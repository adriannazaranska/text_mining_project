import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import csv

def extract_time_period(cells):
    try:
        time_periods = []
        
        # Find the time period table
        time_table = cells[1].find('table')
        if not time_table:
            return None
        
        # Process each semester column
        for sem_col in time_table.find_all('td', class_=lambda x: x and ('sem1' in x or 'sem2' in x)):
            # Determine semester and base number
            semester = 1 if 'sem1' in sem_col.get('class', []) else 2
            base_num = 0 if semester == 1 else 3
            
            # Find all red blocks that aren't hidden
            red_blocks = sem_col.select('div.red:not(.hide)')
            
            for block in red_blocks:
                # Get block number from class (handles block-2 and block-2-3 formats)
                block_class = next((c for c in block.get('class', []) if c.startswith('block-')), None)
                if not block_class:
                    continue
                
                # Extract numbers
                parts = block_class.split('-')[1:]
                if not parts:
                    continue
                
                # Convert to final numbers
                if len(parts) == 1:  # Single block (e.g., block-2)
                    block_num = int(parts[0])
                    time_periods.append(str(base_num + block_num))
                else:  # Range (e.g., block-2-3)
                    start = int(parts[0])
                    end = int(parts[1])
                    time_periods.append(f"{base_num + start}-{base_num + end}")
                    
        return ', '.join(time_periods) if time_periods else None
    
    except Exception as e:
        print(f"Error processing time period: {e}")
        return None

def extract_course_info(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url.strip(), headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract course name
        breadcrumb = soup.find('nav', id='breadcrumb')
        course_name = breadcrumb.find('li', class_='current').find('a').get_text(strip=True) if breadcrumb else None
        
        # Initialize course data (all fields will be strings)
        course_data = {
            'url': url.strip(),
            'course_name': course_name,
            'course_catalogue_number': '',
            'college_graduate': '',
            'language_of_instruction': '',
            'time_period': '',
            'is_part_of': '',
            'course_description': ''
        }

        # Extract table data
        item_info = soup.find('div', class_='item-info')
        if item_info:
            for row in item_info.find_all('tr'):
                cells = row.find_all('td')
                if len(cells) >= 2:
                    label = cells[0].get_text(strip=True).lower()
                    value = cells[1].get_text(strip=True)
                    if 'course catalogue number' in label:
                        course_data['course_catalogue_number'] = value
                    elif 'language of instruction' in label:
                        course_data['language_of_instruction'] = value
                    elif 'time period(s)' in label:
                        course_data['time_period'] = extract_time_period(cells)
                    elif 'college/graduate' in label:
                        course_data['college_graduate'] = value
                    elif 'is part of' in label:
                        links = [link.get_text(strip=True) for link in cells[1].find_all('a')]
                        course_data['is_part_of'] = ', '.join(links) if links else ''

        # Extract description sections
        def extract_section(heading_id, section_name):
            heading = soup.find('h4', id=heading_id)
            if not heading:
                return ''
            
            content = []
            next_elem = heading.find_next_sibling()
            while next_elem and next_elem.name != 'h4':
                if next_elem.name == 'p':
                    content.append(next_elem.get_text(strip=True))
                elif next_elem.name == 'ul':
                    content.extend(li.get_text(strip=True) for li in next_elem.find_all('li'))
                next_elem = next_elem.find_next_sibling()
            
            if content:
                return f"{section_name}: " + ' '.join(content)
            return ''

        objectives = extract_section('leerdoel', 'OBJECTIVES')
        contents = extract_section('inhoud', 'CONTENTS')
        
        # Combine all description parts
        description_parts = [part for part in [objectives, contents] if part]
        if description_parts:
            course_data['course_description'] = '\n'.join(description_parts)

        return course_data

    except Exception as e:
        print(f"Error processing {url.strip()}: {str(e)}")
        return {
            'url': url.strip(),
            'course_name': '',
            'course_catalogue_number': '',
            'college_graduate': '',
            'language_of_instruction': '',
            'is_part_of': '',
            'course_description': '',
            'error': str(e)
        }

def scrape_courses_from_txt(input_txt, output_csv):
    try:
        with open(input_txt, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        results = []
        for url in tqdm(urls, desc="Scraping courses"):
            results.append(extract_course_info(url))
        
        # Convert to DataFrame and save with proper CSV formatting
        df = pd.DataFrame(results)
        
        # Replace None with empty string to avoid issues
        df = df.fillna('')
        
        # Save with quoting all fields and proper encoding
        df.to_csv(
            output_csv,
            index=False,
            quoting=csv.QUOTE_ALL,
            quotechar='"',
            encoding='utf-8-sig'  # For proper special character handling
        )
        print(f"Successfully saved {len(df)} courses to {output_csv}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    scrape_courses_from_txt(
        input_txt="../datasets/uva_course_links.txt",
        output_csv="recommender_dataset.csv"
    )