
import requests ##pip install
import pprint

## ดึงราคาจาก Bx.in.th

def GetBxPrice(Number_to_get = 5):

    data = requests.get('https://bx.in.th/api/')
    # print(type(data))
    ### ทำให้ข้อมูลเป็น dictionary
    data = requests.get('https://bx.in.th/api/').json()
    # print(type(data))

    # pp = pprint.PrettyPrinter(indent=3)

    # pp.pprint(data)
    result = []
    for key in list(data.keys())[0:Number_to_get]:
        prim_name = data[key]['primary_currency']
        sec_name = data[key]['secondary_currency']
        change = data[key]['change']
        last_price = data[key]['last_price']
        volume = data[key]['volume_24hours']
        price_data = {
            'prim_name' : prim_name,
            'sec_name' : sec_name,
            'change' : change,
            'last_price' : last_price,
            'volume' : volume ,
        }

        # price_data = [
        #     prim_name,sec_name,change,last_price,volume ,
        # ]
        result.append(price_data)
        # print(prim_name , change , ' : ' , sec_name , ' : ', last_price , ' : ', change , ' : ', volume)
    return result

if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=3)

    pp.pprint(GetBxPrice())


# if __name__ == '__main__':
#     GetBxPrice()
    
