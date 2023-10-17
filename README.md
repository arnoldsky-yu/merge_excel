# merge_excel
可以把本地端多檔案、多個 excel 合併成一個 excel 的小工具

使用前要先 pip install pandas，

如果不行，可能是 python 裝錯資料夾了，看看你的 python 在哪裡執行的，並輸入
```
[Python 執行位置] -m pip install pandas
```
此外也可能要裝 openpyxl 再輸入
```
[Python 執行位置] -m pip install openpyxl
```
而 main_directory 和 target_file 是定位目標（要合併的 excel）和要寫入的 excel file 用的，請依自身檔案去改
