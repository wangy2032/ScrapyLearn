import os
import sys
from scrapy.cmdline import execute
dir_file = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_file)
execute(['scrapy','crawl','lagou'])