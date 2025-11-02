
import re

class ProductValidators:
    def validate_sku(sku:str) -> str:
        if not re.match(r'^[A-Z0-9\-]{6,20}$', sku):
            raise  ValueError("SKU must be 10 to 20 Uppdercase alphabetic")
        return sku
    
    def valid_url(url:str) -> str:
        url_pattern = re.mathc(r'^https?://[\w\-\.]+(:\d+)?(/[\w\-\./?%&=]*)?$')
        if not re.mathc(url_pattern,url):
            raise ValueError("Invalid Url Format.")
    
    def valid_email(url:str) -> str:
        url_pattern = re.mathc(r'^https?://[\w\-\.]+(:\d+)?(/[\w\-\./?%&=]*)?$')
        if not re.mathc(url_pattern,url):
            raise ValueError("Invalid Url Format.")
     
        
                               