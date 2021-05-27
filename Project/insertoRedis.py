import redis , os , pprint
import pandas as pd  
from getData import get_filedate
from csv import DictReader


def writeOnRedis():


    r = redis.Redis(
    host='192.168.99.100',
    port='6379')


    filedate = get_filedate()
    # filename= 'EQ260521.csv'
    filename= 'EQ' + filedate + '.csv'
    path = f'C:/Users/shubh/Projekt/Project/util/data/{filedate}'
    os.chdir(path)
    data = pd.read_csv(f'{path}/{filename}')
    print(data)
    keep_col = ['SC_CODE', 'SC_NAME', 'OPEN','HIGH','LOW','CLOSE']
    new_f = data[keep_col]
    new_f.to_csv("inputRedis.csv", index=False)
    print("inputRedis.csv - File created successfully")


    # file_handle = open("util\\data\\210521\\inputRedis.csv", "r", encoding="utf-8")
    file_handle = open("inputRedis.csv", "r", encoding="utf-8")
    csv_reader = DictReader(file_handle)

    key_dict_list =[]

    val_dict_list =[]
    for row in csv_reader:
        key_dict_list.append(row['SC_NAME'])
        val_dict_list.append(row)

    file_handle.close()

    def getNameFromlist():
        n = 0 
        while n <= len(key_dict_list):
            val = key_dict_list[n]
            yield val
            n +=1

    name = getNameFromlist()
    data_red= {f"bhavcopy:{next(name)}":i for i in (val_dict_list)}

    pprint.pprint(data_red)

    print("DATA well cooked , now serving to redis")
    with r.pipeline() as pipe:
        for bhavcopy_id, bhavcopy in data_red.items():
            pipe.hmset(bhavcopy_id,bhavcopy)
        pipe.execute()
    
    r.bgsave()
    print("REDIS digested all DATA")
    print(r.hgetall("bhavcopy:VOITH PAPER "))

if __name__ == "__main__":
    writeOnRedis()
