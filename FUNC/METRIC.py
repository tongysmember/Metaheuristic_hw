import datetime
import os, psutil


class metric_time(object):
    '''
    Metric Process Time
    '''
    def __init__(self):
        print('init')
        self.metric_start = None
        self.metric_end = None
    
    def metric_time_start(self):
        self.metric_start = datetime.datetime.now()
        print('metric_time_start:', self.metric_start)
    
    def metric_time_end(self):
        self.metric_end = datetime.datetime.now()
        print('metric_time_end  :', self.metric_end)
    
    def metric_time_calculate(self):
        '''
        Calculate Time Diff and Clear History
        '''
        process_duration = (self.metric_end - self.metric_start)
        self.metric_start = None
        self.metric_end = None
        print('CALCULATE_TIME  :', process_duration)
        #return process_duration

class metric_memory(object):
    '''
    Metric Memory Usage
    '''    
    @staticmethod
    def metric_memory_usage():
        process = psutil.Process(os.getpid())
        print("{0} MB-Memory-Usage".format(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

def main():
    print('main')
    metric_time_obj = metric_time()
    metric_time_obj.metric_time_start()
    metric_time_obj.metric_time_end()
    print(metric_time_obj.metric_time_calculate())

    metric_memory.metric_memory_usage()

    
if __name__ == '__main__':
    main()
        