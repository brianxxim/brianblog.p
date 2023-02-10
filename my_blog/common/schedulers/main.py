from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from .caches import reset_lasting_cache, sync_cache, sync_comment
from .search import reset_search_index

executors = {
    'default': ThreadPoolExecutor(10),
}

scheduler = BackgroundScheduler(executors=executors, timezone='Asia/Shanghai')

# 重置缓存数据
scheduler.add_job(reset_lasting_cache, 'cron', hour=5)
# 从缓存中同步数据到数据库
scheduler.add_job(sync_cache, 'cron', hour=3)
# 从畅言云评同步评论数量到数据库
scheduler.add_job(sync_comment, 'interval', hours=5)
# 更新全部search索引
scheduler.add_job(reset_search_index, 'cron', day_of_week='mon')

# cron: 指定周期 interval: 指定时间间隔
if __name__ == '__main__':
    scheduler.start()
