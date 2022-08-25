from config import Configuration
import schedule
from job import daka
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def init():
    # 读取配置
    Configuration.read_config()
    # 清理日程表
    schedule.clear()
    # 设置日程表
    schedule.every().day.at(Configuration.config["schedule"]).do(daka)


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        init()


def main():
    # 监听 application.yml，当文件内容改变的时候重新加载配置
    observer = Observer()
    file_handler = FileHandler()
    observer.schedule(file_handler, 'application.yml', recursive=True)
    observer.start()
    # 初始化
    init()
    # 主循环
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
