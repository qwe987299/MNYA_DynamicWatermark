# MNYA_DynamicWatermark 萌芽動態浮水印程式

MNYA_DynamicWatermark 是一個用於 MP4 影片產生動態浮水印的小程式。透過 Python 的 moviepy 模組，該程式可為影片加入隨時間改變位置的浮水印，並運用鏡像法則在碰到影片邊緣時反向移動，呈現連續且動態的效果。這個專案適合需要在影片中添加防竄改或個性化浮水印的使用者。

## 專案結構

```

MNYA_DynamicWatermark/
├── .gitignore // 忽略 build、src 與虛擬環境等目錄
├── run.py // 主程式，負責影片處理與動態浮水印合成
├── run.bat // Windows 執行批次檔，方便快速啟動程式
├── start_venv.bat // Windows 建立虛擬環境的批次檔
├── watermark.png // 浮水印圖片，預設浮水印
├── src/ // 原始 MP4 影片目錄，請將待處理的影片放置於此
└── build/ // 處理後影片儲存目錄，產生的影片將輸出至此

```

## 使用方式

1. **環境建置**  
   請先確認已安裝 Python 3。

   - **Windows 使用者**：請直接執行 `start_venv.bat`，該批次檔將自動建立虛擬環境並安裝指定版本的 moviepy（moviepy==1.0.3）。
   - **非 Windows 使用者**：請依下列步驟建立虛擬環境並安裝必要套件：
     ```bash
     python -m venv venv
     source venv/bin/activate   # Linux / MacOS
     python -m pip install moviepy==1.0.3
     ```

2. **準備影片與浮水印**

   - 將欲處理的 MP4 影片放置於 `src/` 目錄中。
   - 如需更換浮水印，請將您自訂的圖片命名為 `watermark.png` 並置於專案根目錄。

3. **執行程式**

   - **進入虛擬環境**  
     請先進入虛擬環境：
     ```bash
     source venv/bin/activate   # Linux / MacOS
     venv\Scripts\activate      # Windows
     ```
   - **啟動程式**  
     進入虛擬環境後，在終端機中執行下列指令啟動程式：
     ```bash
     python run.py
     ```
     或於 Windows 平台上直接執行 `run.bat` 批次檔。  
     執行後，處理完成的影片將自動儲存至 `build/` 目錄中。

4. **檢查結果**  
   請前往 `build/` 目錄確認已添加動態浮水印的影片，並檢視浮水印移動效果是否符合需求。
