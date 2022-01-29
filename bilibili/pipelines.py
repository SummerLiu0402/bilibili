# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter


class BilibiliPipeline(object):
    def open_spider(self, spider):
        print("开始导出")
        self.file = open("./rank.csv","wb")
        self.exporter = CsvItemExporter(self.file, encoding = "utf-8-sig",fields_to_export=["type","rank","up","title","play","like","follow"])
        self.exporter.start_exporting()
    def process_item(self, item, spider):
        item['like'] = replaceBlank(item['like'])
        item['play'] = replaceBlank(item['play'])
        item['up'] = replaceBlank(item['up'])
        item['title'] = replaceBlank(item['title'])
        item['rank'] = replaceBlank(item['rank'])
        item['follow'] = replaceBlank(item['follow'])
        # if len(item['like']) > 0:
        #     item['like'] = item['like'][0].replace('\n', '').replace('\r', '').replace(' ','')
        # if len(item['play']) > 0:
        #     item['play'] = item['play'][0].replace('\n', '').replace('\r', '').replace(' ','')
        # if len(item['up']) > 0:
        #     item['up'] = item['up'][0].replace('\n', '').replace('\r', '').replace(' ','')
        # if len(item['title']) > 0:
        #     item['title'] = item['title'][0].replace('\n', '').replace('\r', '').replace(' ','')
        # if len(item['rank']) > 0:
        #     item['rank'] = item['rank'][0].replace('\n', '').replace('\r', '').replace(' ','')
        # if len(item['follow']) > 0:
        #     item['follow'] = item['follow'][0].replace('\n', '').replace('\r', '').replace(' ','')
        self.exporter.export_item(item)
        return item
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print("结束导出")
def replaceBlank(field):
    if len(field) > 0:
        return field[0].replace('\n', '').replace('\r', '').replace(' ','')
    return ""
