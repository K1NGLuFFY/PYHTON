"""
Web Scraper with Data Analysis Tool
A comprehensive Python tool for web scraping and data analysis
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urljoin, urlparse
import time
import json
import re
from datetime import datetime
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

class WebScraperAnalyzer:
    def __init__(self, base_url=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.scraped_data = []
        self.analysis_results = {}
        
    def scrape_website(self, url, elements=None, max_pages=1):
        """
        Scrape website for specified elements
        Args:
            url (str): Target URL to scrape
            elements (dict): Dictionary of elements to scrape {'name': 'tag.class'}
            max_pages (int): Maximum pages to scrape
        """
        if elements is None:
            elements = {
                'titles': 'h1, h2, h3',
                'paragraphs': 'p',
                'links': 'a[href]',
                'images': 'img[src]'
            }
        
        scraped_data = []
        
        try:
            for page in range(1, max_pages + 1):
                current_url = f"{url}?page={page}" if page > 1 else url
                print(f"Scraping: {current_url}")
                
                response = self.session.get(current_url, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                page_data = {
                    'url': current_url,
                    'timestamp': datetime.now().isoformat(),
                    'page': page
                }
                
                for key, selector in elements.items():
                    elements_found = soup.select(selector)
                    page_data[key] = [elem.get_text(strip=True) if key != 'images' 
                                     else elem.get('src', '') for elem in elements_found]
                    page_data[f'{key}_count'] = len(elements_found)
                
                scraped_data.append(page_data)
                time.sleep(1)  # Be respectful to the server
                
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
            
        self.scraped_data = scraped_data
        return scraped_data
    
    def analyze_text_data(self, text_data):
        """Analyze text data for patterns and insights"""
        if not text_data:
            return {}
        
        # Combine all text
        all_text = ' '.join([item for sublist in text_data for item in sublist])
        
        # Basic text analysis
        words = re.findall(r'\b\w+\b', all_text.lower())
        word_freq = Counter(words)
        
        analysis = {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'most_common_words': word_freq.most_common(20),
            'avg_word_length': np.mean([len(word) for word in words]) if words else 0,
            'text_length': len(all_text),
            'sentence_count': len(re.findall(r'[.!?]+', all_text))
        }
        
        return analysis
    
    def analyze_links(self, links_data):
        """Analyze link patterns and domains"""
        if not links_data:
            return {}
        
        all_links = [item for sublist in links_data for item in sublist]
        domains = [urlparse(link).netloc for link in all_links if link.startswith('http')]
        
        analysis = {
            'total_links': len(all_links),
            'unique_links': len(set(all_links)),
            'domains': Counter(domains).most_common(10),
            'internal_links': len([link for link in all_links if not link.startswith('http')]),
            'external_links': len([link for link in all_links if link.startswith('http')])
        }
        
        return analysis
    
    def create_visualizations(self, data, save_path='analysis_results'):
        """Create visualizations for the scraped data"""
        if not data:
            print("No data to visualize")
            return
        
        # Create directory for results
        import os
        os.makedirs(save_path, exist_ok=True)
        
        # Prepare data for visualization
        df = pd.DataFrame(data)
        
        # 1. Bar chart of element counts
        plt.figure(figsize=(12, 6))
        element_cols = [col for col in df.columns if col.endswith('_count')]
        if element_cols:
            df[element_cols].mean().plot(kind='bar')
            plt.title('Average Element Counts Across Pages')
            plt.xlabel('Element Types')
            plt.ylabel('Average Count')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{save_path}/element_counts.png')
            plt.close()
        
        # 2. Word frequency visualization
        text_data = []
        for page in data:
            if 'paragraphs' in page:
                text_data.extend(page['paragraphs'])
        
        if text_data:
            analysis = self.analyze_text_data([text_data])
            if 'most_common_words' in analysis:
                words, counts = zip(*analysis['most_common_words'][:10])
                plt.figure(figsize=(12, 6))
                plt.bar(words, counts)
                plt.title('Top 10 Most Common Words')
                plt.xlabel('Words')
                plt.ylabel('Frequency')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(f'{save_path}/word_frequency.png')
                plt.close()
        
        print(f"Visualizations saved to {save_path}/")
    
    def export_data(self, filename='scraped_data.json'):
        """Export scraped data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
        print(f"Data exported to {filename}")
    
    def generate_report(self, save_path='analysis_report.txt'):
        """Generate a comprehensive analysis report"""
        if not self.scraped_data:
            print("No data to analyze")
            return
        
        report = []
        report.append("WEB SCRAPING ANALYSIS REPORT")
        report.append("=" * 40)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total pages scraped: {len(self.scraped_data)}")
        report.append("")
        
        # Collect all data for analysis
        all_titles = []
        all_paragraphs = []
        all_links = []
        
        for page in self.scraped_data:
            all_titles.extend(page.get('titles', []))
            all_paragraphs.extend(page.get('paragraphs', []))
            all_links.extend(page.get('links', []))
        
        # Text analysis
        if all_paragraphs:
            text_analysis = self.analyze_text_data([all_paragraphs])
            report.append("TEXT ANALYSIS:")
            report.append(f"  Total words: {text_analysis.get('total_words', 0)}")
            report.append(f"  Unique words: {text_analysis.get('unique_words', 0)}")
            report.append(f"  Average word length: {text_analysis.get('avg_word_length', 0):.2f}")
            report.append(f"  Sentence count: {text_analysis.get('sentence_count', 0)}")
            report.append("")
        
        # Link analysis
        if all_links:
            link_analysis = self.analyze_links(all_links)
            report.append("LINK ANALYSIS:")
            report.append(f"  Total links: {link_analysis.get('total_links', 0)}")
            report.append(f"  Unique links: {link_analysis.get('unique_links', 0)}")
            report.append(f"  External links: {link_analysis.get('external_links', 0)}")
            report.append(f"  Internal links: {link_analysis.get('internal_links', 0)}")
            report.append("")
        
        # Top domains
        if all_links:
            domains = [urlparse(link).netloc for link in all_links if link.startswith('http')]
            top_domains = Counter(domains).most_common(5)
            report.append("TOP DOThe `python/` directory does exist in the current workspace. I will attempt to create the `web_scraper_analyzer.py` file again, ensuring that it is placed in the correct directory.

<create_file>
<path>python/web_scraper_analyzer.py</path>
<content>
"""
Web Scraper with Data Analysis Tool
A comprehensive Python tool for web scraping and data analysis
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urljoin, urlparse
import time
import json
import re
from datetime import datetime
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

class WebScraperAnalyzer:
    def __init__(self, base_url=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.scraped_data = []
        self.analysis_results = {}
        
    def scrape_website(self, url, elements=None, max_pages=1):
        """
        Scrape website for specified elements
        Args:
            url (str): Target URL to scrape
            elements (dict): Dictionary of elements to scrape {'name': 'tag.class'}
            max_pages (int): Maximum pages to scrape
        """
        if elements is None:
            elements = {
                'titles': 'h1, h2, h3',
                'paragraphs': 'p',
                'links': 'a[href]',
                'images': 'img[src]'
            }
        
        scraped_data = []
        
        try:
            for page in range(1, max_pages + 1):
                current_url = f"{url}?page={page}" if page > 1 else url
                print(f"Scraping: {current_url}")
                
                response = self.session.get(current_url, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                page_data = {
                    'url': current_url,
                    'timestamp': datetime.now().isoformat(),
                    'page': page
                }
                
                for key, selector in elements.items():
                    elements_found = soup.select(selector)
                    page_data[key] = [elem.get_text(strip=True) if key != 'images' 
                                     else elem.get('src', '') for elem in elements_found]
                    page_data[f'{key}_count'] = len(elements_found)
                
                scraped_data.append(page_data)
                time.sleep(1)  # Be respectful to the server
                
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
            
        self.scraped_data = scraped_data
        return scraped_data
    
    def analyze_text_data(self, text_data):
        """Analyze text data for patterns and insights"""
        if not text_data:
            return {}
        
        # Combine all text
        all_text = ' '.join([item for sublist in text_data for item in sublist])
        
        # Basic text analysis
        words = re.findall(r'\b\w+\b', all_text.lower())
        word_freq = Counter(words)
        
        analysis = {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'most_common_words': word_freq.most_common(20),
            'avg_word_length': np.mean([len(word) for word in words]) if words else 0,
            'text_length': len(all_text),
            'sentence_count': len(re.findall(r'[.!?]+', all_text))
        }
        
        return analysis
    
    def analyze_links(self, links_data):
        """Analyze link patterns and domains"""
        if not links_data:
            return {}
        
        all_links = [item for sublist in links_data for item in sublist]
        domains = [urlparse(link).netloc for link in all_links if link.startswith('http')]
        
        analysis = {
            'total_links': len(all_links),
            'unique_links': len(set(all_links)),
            'domains': Counter(domains).most_common(10),
            'internal_links': len([link for link in all_links if not link.startswith('http')]),
            'external_links': len([link for link in all_links if link.startswith('http')])
        }
        
        return analysis
    
    def create_visualizations(self, data, save_path='analysis_results'):
        """Create visualizations for the scraped data"""
        if not data:
            print("No data to visualize")
            return
        
        # Create directory for results
        import os
        os.makedirs(save_path, exist_ok=True)
        
        # Prepare data for visualization
        df = pd.DataFrame(data)
        
        # 1. Bar chart of element counts
        plt.figure(figsize=(12, 6))
        element_cols = [col for col in df.columns if col.endswith('_count')]
        if element_cols:
            df[element_cols].mean().plot(kind='bar')
            plt.title('Average Element Counts Across Pages')
            plt.xlabel('Element Types')
            plt.ylabel('Average Count')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{save_path}/element_counts.png')
            plt.close()
        
        # 2. Word frequency visualization
        text_data = []
        for page in data:
            if 'paragraphs' in page:
                text_data.extend(page['paragraphs'])
        
        if text_data:
            analysis = self.analyze_text_data([text_data])
            if 'most_common_words' in analysis:
                words, counts = zip(*analysis['most_common_words'][:10])
                plt.figure(figsize=(12, 6))
                plt.bar(words, counts)
                plt.title('Top 10 Most Common Words')
                plt.xlabel('Words')
                plt.ylabel('Frequency')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(f'{save_path}/word_frequency.png')
                plt.close()
        
        print(f"Visualizations saved to {save_path}/")
    
    def export_data(self, filename='scraped_data.json'):
        """Export scraped data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
        print(f"Data exported to {filename}")
    
    def generate_report(self, save_path='analysis_report.txt'):
        """Generate a comprehensive analysis report"""
        if not self.scraped_data:
            print("No data to analyze")
            return
        
        report = []
        report.append("WEB SCRAPING ANALYSIS REPORT")
        report.append("=" * 40)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total pages scraped: {len(self.scraped_data)}")
        report.append("")
        
        # Collect all data for analysis
        all_titles = []
        all_paragraphs = []
        all_links = []
        
        for page in self.scraped_data:
            all_titles.extend(page.get('titles', []))
            all_paragraphs.extend(page.get('paragraphs', []))
            all_links.extend(page.get('links', []))
        
        # Text analysis
        if all_paragraphs:
            text_analysis = self.analyze_text_data([all_paragraphs])
            report.append("TEXT ANALYSIS:")
            report.append(f"  Total words: {text_analysis.get('total_words', 0)}")
            report.append(f"  Unique words: {text_analysis.get('unique_words', 0)}")
            report.append(f"  Average word length: {text_analysis.get('avg_word_length', 0):.2f}")
            report.append(f"  Sentence count: {text_analysis.get('sentence_count', 0)}")
            report.append("")
        
        # Link analysis
        if all_links:
            link_analysis = self.analyze_links([all_links])
            report.append("LINK ANALYSIS:")
            report.append(f"  Total links: {link_analysis.get('total_links', 0)}")
            report.append(f"  Unique links: {link_analysis.get('unique_links', 0)}")
            report.append(f"  External links: {link_analysis.get('external_links', 0)}")
            report.append(f"  Internal links: {link_analysis.get('internal_links', 0)}")
            report.append("")
        
        # Top domains
        if all_links:
            domains = [urlparse(link).netloc for link in all_links if link.startswith('http')]
            top_domains = Counter(domains).most_common(5)
            report.append("TOP DOMAINS:")
            for domain, count in top_domains:
                report.append(f"  {domain}: {count} links")
            report.append("")
        
        # Save report
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        print(f"Report saved to {save_path}")
        print('\n'.join(report))

def demo_usage():
    """Demonstrate the web scraper functionality"""
    scraper = WebScraperAnalyzer()
    
    # Example usage with a test website
    test_url = "https://httpbin.org/html"  # Safe test URL
    
    print("Web Scraper with Data Analysis Demo")
    print("=" * 40)
    
    # Scrape data
    data = scraper.scrape_website(test_url, max_pages=1)
    
    if data:
        # Export data
        scraper.export_data('demo_scraped_data.json')
        
        # Generate report
        scraper.generate_report()
        
        # Create visualizations
        scraper.create_visualizations(data)
        
        print("Demo completed successfully!")
    else:
        print("No data scraped. Check your internet connection and URL.")

if __name__ == "__main__":
    demo_usage()
