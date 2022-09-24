print ("""

Kullanıcı Girişi

""")

sys_kullanıcı_adı  = "murat"
anne_soyadı ="meral"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
kullanıcı_anne_soyadı = input (" kullanıcı soyadı:")
parola = input ("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("parola hatalı.....")
elif( kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola ):
    print("Kullanıcı Adı Hatalı...")
elif(anne_soyadı != kullanıcı_anne_soyadı and kullanıcı_adı == sys_kullanıcı_adı and sys_parola == parola):
    print("anne soyadı hatalı")
elif( kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola ):
     print ("Kullanıcı Adı ve Parola hatalı..... ")
else:
    print("sisteme başarı ile giriş yapıldı.....")