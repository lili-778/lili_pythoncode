import yaml
# from base_method import Base_Method
from app_Automation_2.podemo.base.base_method import Base_Method


class Generate_Data():
    # 自动生成n条姓名和手机号码数据，并保存到data文件夹下
    def gene_name_phone(n):
        data=[]
        for i in range(n):
            name=Base_Method.get_name()
            phone=Base_Method.get_phone()
            tup=(name,phone)
            data.append(tup)
        # w模式每次执行会重新覆盖原先的数据
        with open('../data/name_phone.yaml','w',encoding="utf-8") as f:
            yaml.safe_dump(data,f,allow_unicode=True)
        with open('../data/name_phone.yaml','r',encoding="utf-8") as f:
            data=yaml.safe_load(f)
        return data

if __name__=="__main__":
    print(Generate_Data.gene_name_phone(2))
