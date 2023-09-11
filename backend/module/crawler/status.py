class CrawlerStatus:
    def __init__(self):
        self.is_permitted = False
        self.total_num = 0
        self.total_page = 0
        self.current_page = 0
        self.current_time = 0
        self.status = []
        self.current_task = []

    def print_status(self):
        return self.status
    
    def set_status(self, status):
        self.status.append(status)
    
    def get_status(self):
        return self.status
