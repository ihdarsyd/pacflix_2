from tabulate import tabulate

class User:
    # Data User
    data_user = {
        1: ["Rosy", "Basic Plan", 12, 'rosy-123'],
        2: ["Anton", "Standard Plan", 9, 'anton-123'],
        3: ["Agus", "Basic Plan", 1, 'agus-123'],
        4: ["Budi", "Premium Plan", 5, 'budi-123'],
        5: ["Shania", "Basic Plan", 6, 'shania-123']
    }

    print("test")
    # Data list_plan
    list_plan = ["Basic Plan", "Standard Plan", "Premium Plan"]
    list_benefit = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]] # data
    headers =  ["Basic Plan", "Standard Plan", "Premium Plan", "Services"] # header atau nama kolom

    
    
    def __init__(self, username):
        """
        Fungsi ini digunakan untuk menginisialisasi objek User

        input: username (str)
        """
        self.username = username
        self.current_plan = None
        self.duration_plan = None
        self.kode_referral = None

        for key, value in self.data_user.items():
            if value[0] == self.username:
                self.current_plan = value[1]
                self.duration_plan = value[2]
                self.kode_referral = value[3]
                break

    def check_all_plan(self):
        """
        Fungsi ini digunakan untuk mencetak plan dan benefit 

        input: None
        """
        print("List Benefit and Plan from Pacflix")
        print("")
        print(tabulate(self.list_benefit, self.headers))

    def check_user_plan(self):
        """
        Fungsi untuk menampilkan plan dan benefit dari current_plan user
        """

        if(self.current_plan):
            print(f"{self.username} sedang berlangganan {self.current_plan}")
            print("Benefit")

            idx_current_plan = self.list_plan.index(self.current_plan)
            headers_user = [self.headers[idx_current_plan],self.headers[-1]]
            benefit_user = [[row[idx_current_plan], row[-1]] for row in self.list_benefit]
            print(tabulate(benefit_user, headers_user))
        else:
            print("anda belum berlangganan")

    def upgrade_plan(self,new_plan):
        """
        Fungsi untuk melakukan upgrade plan baru

        input: new_plan(str)
        """
        if(self.current_plan is not None and new_plan in self.list_plan):
            idx_current_plan = self.list_plan.index(self.current_plan)
            idx_new_plan = self.list_plan.index(new_plan)

            if(idx_new_plan > idx_current_plan):
                # Do upgrade
                if (self.duration_plan > 12):
                    # mendapatkan diskon
                    total = self.list_benefit[-1][idx_new_plan] - (self.list_benefit[-1][idx_new_plan]*0.05)
                else:
                    total = self.list_benefit[-1][idx_new_plan]
                print(f"Harga Upgrade ke {new_plan} adalah Rp.{total}")

                #Update data user
                self.current_plan = new_plan
                for key, value in self.data_user.items():
                    if(self.username == value[0]):
                        self.data_user[key][1] = new_plan
                        break

            elif(idx_current_plan == idx_new_plan):
                print(f"Anda sedang berlangganan {new_plan}")
            else:
                print(f"Anda tidak downgrade ke {new_plan}")
        elif(new_plan not in self.list_plan) :
            print("New Plan tidak tersedia")
        elif(self.current_plan is None):
            print("Silakan berlangganan terlebih dahulu")       


    def subs_plan(self, new_plan, kode_referral):
        """
        Fungsi untuk melakukan subscribe plan bagi user baru

        input:
            - new_plan (str)
            - kode_referral (str)
        """
        list_code = [x[-1] for x in self.data_user.values()]
        # list_code = []

        # for x in self.data_user.values():
        #     list_code.append(x[-1])

        if(self.current_plan is None):

            if(new_plan in self.list_plan):
                # do subs
                self.current_plan = new_plan
                self.duration_plan = 1
                self.kode_referral =  f"{self.username}-123"
                
                idx_new_plan = self.list_plan.index(new_plan)
                #menampilkan harganya
                if(kode_referral in list_code):
                    # dapat diskon
                    total = self.list_benefit[-1][idx_new_plan] - (self.list_benefit[-1][idx_new_plan] * 0.04)
                    
                else:
                    # harga normal
                    total = self.list_benefit[-1][idx_new_plan]
                print(f"Harga yang harus dibayarkan untuk subs {new_plan} adalah Rp.{total}")

                # Tambahakan user baru
                last_key = max(self.data_user.keys())
                self.data_user[last_key+1] = [self.username,self.current_plan,self.duration_plan,self.kode_referral]

            else:
                print("Plan tidak Tersedia")
        else:
            print("Anda sudah memiliki plan")