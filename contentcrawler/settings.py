# -*- coding: utf-8 -*-

# Scrapy settings for contentcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'contentcrawler'

SPIDER_MODULES = ['contentcrawler.spiders']
NEWSPIDER_MODULE = 'contentcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'contentcrawler (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'contentcrawler.pipelines.JsonExportPipeline': 300
}
LOG_LEVEL='INFO'
