# pip3 install python3-memcached
import memcache

class MemcachedHelper():

    def __init__(self,ip,port):
        connect = str(ip) + ':' + str(port)
        self.mc = memcache.Client([connect], debug=0)

    def set_key(self,key,value):
        return self.mc.set(key,value)

    def get_key(self,key):
        return self.mc.get(key)

    def delte_key(self,key):
        return self.mc.delete(key)

    def incr_key(self,key):
        return self.mc.incr(key)

    def decr_key(self,key):
        return self.mc.decr(key)

    def set_muti(self,keys_values_dict):
        return self.mc.set_multi(keys_values_dict)

    def get_multi(self,keys_list):
        return self.mc.get_multi(keys_list)

    def del_multi(self,keys_list):
        return self.mc.delete_multi(keys_list)

    def get_stats(self):
        return self.mc.get_stats()[0][1]

    def print_stats_info(self):
        print(self.mc.get_stats())
        stats_dict = self.mc.get_stats()[0]
        for key in stats_dict:
            print("%s , %s" % (key.decode(encoding='utf-8'), stats_dict[key].decode(encoding='utf-8')))

    def get_stats_info(self,name):
        return self.mc.get_stats()[0][1][name.encode(encoding="utf-8")].decode(encoding='utf-8')

    def get_info_cmd_set(self):
        return self.mc.get_stats()[0][1][b'cmd_set'].decode(encoding='utf-8')



def main():
    mh = MemcachedHelper('192.168.196.129',11211)

    mh.print_stats_info()

    print("==============================")

    print("curr_items = %s" % mh.get_stats_info('curr_items'))

if __name__ == '__main__':
    main()