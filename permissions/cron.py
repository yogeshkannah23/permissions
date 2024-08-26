from .models import Post
import logging

# logging.basicConfig(filename="/home/ss-pr-cpu-398ha/Desktop/permissions/log.log", level=logging.INFO)

logging.basicConfig(
    filename="/home/ss-pr-cpu-398ha/Desktop/permissions/log.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def my_scheduled_job():
    post = Post.objects.create(title="name",discription="yogeshkannah")
    post.save()
    logging.info('Model saved')
    print("From the cron tab")