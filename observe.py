import  redis
class Task():
    def __init__(self):
        self.room=redis.Redis(host='127.0.0.1',db=3)
        self.ps=self.room.pubsub()
        self.ps.subscribe=('taskdata:queue-subscribe')
    def process_item(self):
        for item in self.ps.listen():
            if item['type']=='message':
                print('监听到的数据:',item['data'])

Task().process_item()