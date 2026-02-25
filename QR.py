import qrcode

upi_id = input("enter your upi id = ")

# this is how the QR will generate from upi id
phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# this is for make the QR code form url
googlepay_upi = qrcode.make(googlepay_url)
phonepay_upi = qrcode.make(phonepay_url)
paytm_upi = qrcode.make(paytm_url)

# this is for save the QR code 
googlepay_upi.save('googlepay_url.png')
phonepay_upi.save('phonepay_url.png')
paytm_upi.save('paytm_url.png')


googlepay_upi.show()
phonepay_upi.show()
paytm_upi.show()