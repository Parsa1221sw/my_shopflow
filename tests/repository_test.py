from app.services.product_service import Product_Service


def test_repository_product_repository_class():
    service = Product_Service()
    service.get_data_from_repository()
    obj =service.find_product_by_id(1)
    service.add_product(7 , "air pod" , "tecknologia" , 120 , 99.99 , "color : wite  , nois canceling")
    service.remove_product(1)
    service.update_product(2 ,name = "ps3")
    service.change_quantity(2 , 3000)