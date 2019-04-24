## story_001
* greeting
  - utter_greet
* post_query
  - utter_post_query
* product_price{"model" : "iphone x"}
  - slot{"model" : "iphone x"}
  - get_product_price
  - slot{"price": "1828"}
* product_buy{"quantity" : "2"}
  - slot{"quantity" : "2"}
  - confirm_buy
* show_policy
  - utter_check_policy
* payment_method
  - utter_payment_query
* bye
  - utter_bye

## story_002
* greeting
  - utter_greet
* product_storage{"brand": "samsung" , "model": "galaxy s8 plus"}
  - slot{"brand": "samsung"}
  - slot{"model": "galaxy s8 plus"}
  - get_product_storage
  - slot{"ROM": "64 GB"}
* product_price{"brand": "samsung" , "model": "galaxy s8 plus"}
  - slot{"brand": "samsung"}
  - slot{"model" : "galaxy s8 plus"}
  - get_product_price
  - slot{"price": "895"}
* show_policy
  - utter_check_policy
* package_query
  - utter_package_query
* post_query
  - utter_post_query
* payment_method
  - utter_payment_query

## story_003
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city":"Melbourne" , "state":"Victoria"}
  - slot{"city":"Melbourne" , "state":"Victoria"}
  - utter_confirm
* product_price{"brand": "motorola", "model": "moto x g1"}
  - slot{"brand": "motorola"}
  - slot{"model": "moto x g1"}
  - get_product_price
  - slot{"price": "289"}
* product_storage{"model": "moto x g1"}
  - slot{"model" : "moto x g1"}
  - get_product_storage
  - slot{"ROM": "16 GB"}
* product_buy{"model": "moto x g1"}
  - slot{"model": "moto x g1"}
  - confirm_buy
* payment_method
  - utter_payment_query
* post_query
  - utter_post_query
* package_query
  - utter_package_query

## story_004
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city": "brisbane" , "state": "Queensland"}
  - slot{"city": "brisbane"}
  - slot{"state": "Queensland"}
  - utter_confirm
* product_sell
  - utter_ask_product
* product_price{"model": "g6"}
  - slot{"model": "g6"}
  - get_product_price
  - slot{"price": "476"}
* payment_method
  - utter_payment_query
* package_query
  - utter_package_query
* post_query
  - utter_post_query

## story_005
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city": "Darwin", "state": "Northern Territory"}
  - slot{"city": "Darwin"}
  - slot{"state": "Northern Territory"}
  - utter_confirm
* registration_details
  - utter_registration_query
* bye
  - utter_bye

## story_006
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city": "Darwin" , "state": "Northern Territory"}
  - slot{"city": "Darwin"} 
  - slot{"state": "Northern Territory"}
  - utter_confirm
* product_price{"model": "iphone 7"}
  - slot{"model": "iphone 7"}
  - get_product_price
  - slot{"price": "699"}
* show_policy
  - utter_check_policy

## story_007
* greeting
  - utter_greet
  - utter_ask_address
* show_policy
  - utter_check_policy

## story_008
* product_price{"brand": "apple", "model": "iphone 7"}
  - slot{"brand": "apple"}
  - slot{"model": "iphone 7"}
  - get_product_price
  - slot{"price": "699"}

## story_009
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city": "Adelaide"}
  - slot{"city": "Adelaide"}
  - utter_confirm
* product_storage{"brand": "samsung", "model": "galaxy a5"}
  - slot{"brand": "samsung"}
  - slot{"model": "galaxy a5"}
  - get_product_storage
  - slot{"ROM": "32 GB"}
* product_color{"brand": "samsung", "model": "galaxy a5", "color": "black"}
  - slot{"brand": "samsung"} 
  - slot{"model": "galaxy a5"}
  - slot{"color": "black"}
  - get_product_color
  - slot{"color": "black"}
* show_policy
  - utter_check_policy
* bye
  - utter_bye

## story_010
* greeting
  - utter_greet
  - utter_ask_address
* customer_address{"city": "Canberra"}
  - slot{"city": "Canberra"}
  - utter_confirm
* product_storage{"brand": "htc", "model": "one m9"}
  - slot{"brand": "htc"}
  - slot{"model": "one m9"}
  - get_product_storage
  - slot{"ROM": ""}
  - utter_offer 
* affirmative
  - utter_ask_product
* product_buy{"brand": "apple", "model": "iphone x"}
  - slot{"brand": "apple"}
  - slot{"model": "iphone x"}
  - confirm_buy
* show_policy
  - utter_check_policy
* bye
  - utter_bye

## story_011
* greeting
  - utter_greet
  - utter_ask_product
* product_ask{"model": "moto x g1"}
  - slot{"model": "moto x g1"}
  - confirm_buy
* product_buy
  - confirm_buy
* product_buy{"model": "moto x g1"}
  - slot{"model": "moto x g1"}
  - confirm_buy
* payment_method
  - utter_payment_query
* bye
  - utter_bye

## Generated Story 4865347784937034519
* greeting
    - utter_greet
* product_buy
    - utter_ask_product
* product_price{"brand": "samsung", "model": "galaxy a5"}
    - slot{"brand": "samsung"}
    - slot{"model": "galaxy a5"}
    - get_product_price
    - slot{"price": 345}
* product_storage{"brand": "samsung", "model": "galaxy a5"}
    - slot{"brand": "samsung"}
    - slot{"model": "galaxy a5"}
    - get_product_storage
    - slot{"ROM": "32 GB"}
* show_policy
    - utter_check_policy
* product_color
    - get_product_color
    - slot{"color": "black"}
* package_query
    - utter_package_query
* payment_method
    - utter_payment_query
* choice_other
    - utter_offer
* product_price{"brand": "sony", "model": "xperia z3"}
    - slot{"brand": "sony"}
    - slot{"model": "xperia z3"}
    - get_product_price
    - slot{"price": 249}
* product_storage
    - get_product_storage
    - slot{"ROM": "16 GB"}
* product_buy
    - confirm_buy
* show_policy
    - utter_check_policy
* bye
    - utter_bye

## Generated Story 5120958502873924006
* greeting
    - utter_greet
    - utter_ask_address
* customer_address{"city": "Adelaide"}
    - slot{"city": "Adelaide"}
    - utter_confirm
* product_sell
    - utter_ask_product
* product_buy{"brand": "htc", "model": "one m9"}
    - slot{"brand": "htc"}
    - slot{"model": "one m9"}
    - confirm_buy
* payment_method
    - utter_payment_query
* bye
    - utter_bye

## story_012
* greeting
    - utter_greet
* product_complain
    - utter_invoice_id
* product_complain
    - utter_invoice_id
* product_complain{"invoice_id": "ya123"}
    - slot{"invoice_id": "ya123"}
    - forward_complain
    - slot{"complain_id": "3"}
## Generated Story -7598489508093915255
* greeting
    - utter_greet
    - utter_ask_address
* customer_address{"city": "Hobart", "state": "Tasmania"}
    - slot{"city": "Hobart"}
    - slot{"state": "Tasmania"}
    - utter_confirm
* product_complain{"date": "22 February"}
    - slot{"date": "22 February"}
    - forward_complain
* product_complain{"invoice_id": "fu666"}
    - slot{"invoice_id": "fu666"}
    - forward_complain
    - slot{"complain_id": "2"}
* bye
    - utter_confirm
* bye
    - utter_bye

