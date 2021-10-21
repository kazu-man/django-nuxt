
class module:
    def getChartData(totalPriceDate,items): 

        for price in totalPriceDate:
            for item in items.data:
                if price['purchase_date'].strftime('%Y-%m-%d') == item['purchase_date']:
                    
                    if not item["categories"]:
                        emptyData = {"id":-1,"name":"その他","color":"gray","price":item["price"],"purchase_date":item["purchase_date"]}
                        if 'categories' not in price:
                            list = []
                            list.append(emptyData)
                            price['categories'] = list                        
                        else:
                            price['categories'].append(emptyData)
                        print(price)
                        continue


                    for cate in item['categories']:
                        if 'categories' not in price:
                            list = []
                            cate["price"] = item['price']
                            list.append(cate)
                            price['categories'] = list                        
                        else:
                            same_flg = False
                            for each in price['categories']:
                                if cate["id"] == each["id"]:
                                    same_flg = True
                                    each["price"] = int(each["price"]) + int(item["price"])
                                    break
                            if same_flg == False:
                                cate["price"] = item['price']
                                price['categories'].append(cate)
        return totalPriceDate

    def getMonthChartData(totalPriceDate,items): 

        eachDateData = module.getChartData(totalPriceDate,items)
        result = {}
        for eachData in eachDateData:
            for data in eachData["categories"]:
                if 'categories' not in result:
                    list = []
                    list.append(data)
                    result['categories'] = list                        

                else:
                    same_flg = False
                    for each in result["categories"]:
                        if data["id"] == each["id"]:
                            same_flg = True
                            each["price"] = int(each["price"]) + int(data["price"])
                            break

                    if same_flg == False:
                        result['categories'].append(data)


        return result