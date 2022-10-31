from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER_PATH = './chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://suf.purs.gov.rs/v/?vl=A1I3S0dZQ1hNUjdLR1lDWE1IgAAA5HsAAGCYPQYAAAAAAAABhC3dVCwAAABNv%2FFRFdxQNq0mixnUo%2BBRv94Ooh%2BNbslAK6NuNCdifzt78jfw%2FN68s6LnoFz5GC5eMPrbn5wNZ57HjDl9el%2Bh%2FJSFzK%2FEcYFiTYmBQ0QPH9O2%2FtamrVbDTSv1I1YZmDgNUkEJBlA8QBO%2BE3OhHdy6n4TIQG2Coa6uQQVxqgqW8LNaWnMGc8VrPtjt3aFBil45xIX686ghKbsOG5867eZOnehI2GHGAPoO0mdDxT70IK4TssJ0YzY8bCJB5TZHxEDU7XU5eJ0VD7GT2sWO6mOyZWDvsQAuwFMaVzY6qBSVcwkW%2FjUZaAbyFcisqqNlA1K6vcAVaDqe%2F52Aw3LL61X4gLuCVBirMAnO8ftZvFX09XCCsmAquVt45uG2e4RZC4ERPm6TKs35I6%2BHlFRu3jS7XtM2Ba%2FNL3St0TwNThNBMnSpHBsUjO34Nyf6SN%2B0OFYC9SkXevtoKQtsUDF5rNc8LTg414R4YS6QAvpm7bEVfhHkxzDqkDrdGgh%2F0LP1kbeadh7BiARuOIR23cyJ2yE%2FKy1WliI3mVpiQVP3jS2ZUzvCyS2JY0E%2B2qwHvxiMcAvKS5KFFCct50%2BpTPYuL1YKWDOSUwIixMA%2F7o8Mh0MhyTCLbgjlPkd1j0etYhhxJo6XLfOad9JfjU09BtA8IoOSl8ni6z3G%2FYknzWh8qcLQfk5uh3fvWR01zfUnzL7DAaI%3D")
#print(driver.page_source)
iznos = driver.find_element(By.XPATH, "//*[contains(text(),'Укупан износ')]/../div[@class='col-md-12']")
print(iznos.text)
driver.quit()