import csv
import sys

args = sys.argv


def search_and_calculate_sales(file_path, drug_name):
    sales = 0
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # 検索と売上計算
        for i, row in enumerate(rows):
            if i == 0:
                # ヘッダ行の場合、次の行に進む
                continue

            drug_price = float(row[6])  # G列の値
            total_price = float(row[8])  # I列の値
            drug_description = row[3]  # D列の値

            if drug_name in drug_description:
                print(drug_description)
                sales += drug_price * total_price

    return sales

def format_currency(number):
    if number >= 100000000:  # 億以上の場合
        result = f'{number // 100000000}億{number % 100000000 // 10000000}千万円'
    elif number >= 10000000:  # 千万以上の場合
        result = f'{number // 10000000}千万円'
    else:
        result = f'{number}円'
    
    return result

# ファイルパスと薬の名前を指定して売上を計算
#内服薬
internal_external_file_path = '院外.csv'
internal_internal_file_path = '院内.csv'
internal_hospital_file_path = '入院.csv'

#注射薬
injection_external_file_path = '注射_院外.csv'
injection_internal_file_path = '注射_院内.csv'
injection_hospital_file_path = '注射_入院.csv'

#外用薬
topical_external_file_path = '外用_院外.csv'
topical_internal_file_path = '外用_院内.csv'
topical_hospital_file_path = '外用_入院.csv'

drug_name = args[1]

print("院外処方：")
internal_external_sales = search_and_calculate_sales(internal_external_file_path, drug_name)
injection_external_sales = search_and_calculate_sales(injection_external_file_path, drug_name)
topical_external_sales = search_and_calculate_sales(topical_external_file_path, drug_name)
total_external_sales = internal_external_sales + injection_external_sales + topical_external_sales

print("院内処方：")
internal_internal_sales = search_and_calculate_sales(internal_internal_file_path, drug_name)
injection_internal_sales = search_and_calculate_sales(injection_internal_file_path, drug_name)
topical_internal_sales = search_and_calculate_sales(topical_internal_file_path, drug_name)
total_internal_sales = internal_internal_sales + injection_internal_sales + topical_internal_sales

print("入院処方：")
internal_hospital_sales = search_and_calculate_sales(internal_hospital_file_path, drug_name)
injection_hospital_sales = search_and_calculate_sales(injection_hospital_file_path, drug_name)
topical_hospital_sales = search_and_calculate_sales(topical_hospital_file_path, drug_name)
total_hospital_sales = internal_hospital_sales + injection_hospital_sales + topical_hospital_sales

total_sales = total_external_sales + total_internal_sales + total_hospital_sales

total_external_sales = format_currency(int(total_external_sales))
total_internal_sales = format_currency(int(total_internal_sales))
total_hospital_sales = format_currency(int(total_hospital_sales))

total_sales = format_currency(int(total_sales))

print("院外処方売上:", total_external_sales)
print("院内処方売上:", total_internal_sales)
print("入院処方売上:", total_hospital_sales)
print("総売上:", total_sales)