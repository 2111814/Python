from datetime import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo:int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
        
    def timVTDvTheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    def xoaSVTheoMssv(self, maSo:int) -> bool:
        vt = self.timVTDvTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str):
        pass

    def timSvSinhTruocNgay(self, ngay: datetime):
        pass

sv1 = SinhVien(1957690,"Trần Văn A",datetime.strptime("23/6/1999","%d/%m/%Y"))
dssv = DanhSachSV()
dssv.themSinhVien(sv1)
dssv.xuat()

f = open("demo.txt", "r")
print(f.read())






