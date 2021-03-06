import sqlite3

connection = sqlite3.connect('items.db')
c = connection.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS items(item_id TEXT PRIMARY KEY,item_id_num INT, item_name TEXT UNIQUE, price INT)")

create_table()

def sql_insert_item(item_id, item_id_num, item_name, price):
    try:
        sql = """INSERT INTO items(item_id, item_id_num, item_name, price ) VALUES ("{}", "{}", "{}", "{}");""".format(item_id, item_id_num, item_name, price)
        c.execute(sql)
        connection.commit()
    except:
        pass

sql_insert_item("veeta", 1, "جبنة فيتا", 4.0)
sql_insert_item("baket_botatos", 2, "باكيت بطاطس", 7.0)
sql_insert_item("neston", 3, "جبنة نستون", 5.0 )
sql_insert_item("cery", 4,"جبنة كيري", 6.0 )
sql_insert_item("roomy_cheese", 5, "جبنة رومي", 6.0 )
sql_insert_item("roomy_lanchon", 6, "رومي علي لانشون", 6.0 )
sql_insert_item("veeta_keshta", 7,"جبنة فيتا علي قشطة", 6.0 )
sql_insert_item("lanchon", 8, "لانشون", 6.0)
sql_insert_item("beef", 9,"بيف سادة", 6.0 )
sql_insert_item("sandwich_sohba", 10, "ساندويتش صحبة", 6.0)
sql_insert_item("mix_meats", 11, "ميكس لحوم", 6.0)
sql_insert_item("omlet_neston", 12, "أومليت نستون", 6.0)
sql_insert_item("omlet_lanchon", 13, "أومليت لانشون", 6.0)
sql_insert_item("roomy_cery_farm", 14, "رومي كيري فارم", 6.0 )
sql_insert_item("roomy_cery", 15,"رومي علي كيري", 6.0)
sql_insert_item("lanchon_veta",16,"لانشون علي فيتا", 6.0)
sql_insert_item("veeta_eggs",17,"بيض علي فيتا", 6.0)
sql_insert_item("rolls_mekseeky",18,"رولز مكسيكي", 6.0)
sql_insert_item("cheese_makli",19,"جبنة مقلية", 6.0)
sql_insert_item("foul", 20, "فول", 6.0)
sql_insert_item("foul_ta3", 21, "فول علي طعمية", 6.0)
sql_insert_item("foul_sogok",22,"فول سجق", 6.0)
sql_insert_item("eggs_rolls_big",23,"بيض رولز كبير",6.0)
sql_insert_item("eggs_rolls_small",24,"بيض رولز صغير",6.0)
sql_insert_item("foul_zebda",25,"فول زيدة",6.0)
sql_insert_item("foul_neston",26,"فول نستون",6.0)
sql_insert_item("foul_eggs",27,"فول بيض",6.0)
sql_insert_item("foul_keshta",28,"فول قشطة",6.0)
sql_insert_item("ta3",29,"طعمية",6.0)
sql_insert_item("ta3_chebs",30,"طعمية علي شيبسي",6.0)
sql_insert_item("botatos_clo_slo",31,"بطاطس كول سلو", 6.0)
sql_insert_item("omlet_egg",32,"بيض أومليت", 6.0)
sql_insert_item("neston_eggs",33,"بيض علي نستون",6.0)
sql_insert_item("ta3_eggs", 34, "بيض علي طعمية", 6.0)
sql_insert_item("chebs",35,"شيبسي", 6.0)
sql_insert_item("botatos_farm ", 36, "بطاطس فارم", 6.0)
sql_insert_item("omlet_farm", 37, "أومليت فارم", 6.0)
sql_insert_item("boiled_eggs", 38,"بيض مسلوق سادة", 6.0)
sql_insert_item("halawa_sada",39,"حلاوة سادة", 6.0)
sql_insert_item("halawa_keshta", 40, "حلاوة قشطة", 6.0)
sql_insert_item("halawa_cery", 41, "حلاوة علي كيري", 6.0)
sql_insert_item("meraba_sada", 42,"مربي سادة", 6.0)
sql_insert_item("meraba_keshta",43,"مربي قشطة", 6.0)
sql_insert_item("meraba_cery",44,"مربي كيري", 6.0)
sql_insert_item("hunny_sada", 45, "عسل سادة", 6.0)
sql_insert_item("hunny_keshta", 46, "عسل قشطة", 6.0)
sql_insert_item("hunny_cery", 47, "عسل كيري", 6.0)
sql_insert_item("kokteil_helw",48, "كوكتيل حلو سكلانس", 6.0)
sql_insert_item("borger_sada", 49, "برجر سادة", 6.0)
sql_insert_item("borger_eggs", 50, "برجر بيض", 6.0)
sql_insert_item("borger_eggs_roomy", 51, "برجر بيض علي رومي", 6.0)
sql_insert_item("kofta_sada", 52, "كفتة سادة", 6.0)
sql_insert_item("kebda", 53, "كبدة", 6.0)
sql_insert_item("checken_baneh", 54, "فراخ بانيه", 6.0)
sql_insert_item("roomy_baneh", 55, "بانيه علي رومي", 6.0)
sql_insert_item("cheese_borger_double", 56, "تشيز برجر دوبل", 6.0)
sql_insert_item("farm_nar", 57, "فارم علي النار", 6.0)
sql_insert_item("alagreek", 58, "الاجريك", 6.0)
sql_insert_item("ta3_nar", 59, "طعمية نار", 6.0)
sql_insert_item("roomy_cheese_nar", 60, "جبنة رومي نار", 6.0)
sql_insert_item("lanchon_nar", 61,"لانشون نار", 6.0)
sql_insert_item("roomy_cery_chebs_nar", 62, "رومي + كيري + شيبسي نار", 6.0)
sql_insert_item("roomy_lanchon_nar", 63, "رومي علي لانشون نار", 6.0)
sql_insert_item("kresby", 64, "كرسبي", 6.0)
sql_insert_item("cheese_kresby", 65, "كرسبي جبنة", 6.0)
sql_insert_item("kebda_eskandarany", 66, "كبدة اسكندراني", 6.0)
sql_insert_item("borger_double", 67, "برجر دوبل", 6.0)
sql_insert_item("borger_farm", 68, "برجر فارم", 6.0)
