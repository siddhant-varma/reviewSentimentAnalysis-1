try:
	from reviewSetimentAnalysis import Scraper, Analysis
except ImportError:
	from __init__ import Scraper, Analysis
#Paste Urls here
urls = [
	'https://www.amazon.in/Asian-Paints-Terrace-Waterproofing-Coating/dp/B08BWXY8W8/ref=sr_1_2_sspa?dchild=1&keywords=asian+paints+diy&qid=1599815908&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLMkY0STQ3SlpaQzkmZW5jcnlwdGVkSWQ9QTAwMDQ4NjFENEI5Vks5NDg3Q0cmZW5jcnlwdGVkQWRJZD1BMDA0NTkyNlQ3RkJHM09PWDVHMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
	'https://www.amazon.in/Asian-Paints-RustShield-Aerosol-Protection/dp/B08BWZ9GYT/ref=redir_mobile_desktop?ie=UTF8&aaxitk=gMfv-E0wviWuxt3vNXiVGQ&hsa_cr_id=6590193470702&ref_=sbx_be_s_sparkle_mcd_asin_0',
		'https://www.amazon.in/Asian-Paints-ezyCR8-Apcolite-Aerosol/dp/B08G53KX3B/ref=sr_1_3_sspa?dchild=1&keywords=asian+paints+diy&qid=1599815931&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNjVNQ040Uzc5RFJRJmVuY3J5cHRlZElkPUEwNTA1NDExMU9RV1hVNDNFVDBFNyZlbmNyeXB0ZWRBZElkPUEwMjc4NzM3MUJRS0cwMjRUN1Q2NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
		'https://www.amazon.in/Asian-Paints-ezyCR8-Bathroom-Kitchen/dp/B08BWW42C6/ref=sr_1_5?dchild=1&keywords=asian+paints+diy&qid=1599815931&sr=8-5',
		'https://www.amazon.in/Asian-Paints-TruCare-Painting-Masking/dp/B08BWRNRVW/ref=sr_1_6?dchild=1&keywords=asian+paints+diy&qid=1599815931&sr=8-6',
		'https://www.amazon.in/Asian-Paints-RustShield-Aerosol-Protection/dp/B08BWZ9GYT/ref=sr_1_7?dchild=1&keywords=asian+paints+diy&qid=1599815931&sr=8-7',
		#'https://www.flipkart.com/search?q=diy%20asian%20paints%20ezycr8&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',
		'https://www.flipkart.com/asian-paints-ezycr8-apcolite-diy-aerosol-enamel-paint-spray-400-ml-white-spray/p/itm080b12853d5c7?pid=SPYFT32HECGJTFZU&lid=LSTSPYFT32HECGJTFZUQ23GQJ&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&iid=dbae980a-bdad-46b8-a63c-4917774c4c14.SPYFT32HECGJTFZU.SEARCH&ppt=sp&ppn=sp&ssid=muxfiknilc0000001599816814005&qH=18cad6cea86262ae',
		'https://www.flipkart.com/asian-paints-ezycr8-diy-aerosol-spray-rust-removal-protection-400-ml-clear-spray-paint/p/itm27b5fe9ea4182?pid=SPYFT28C83GYFSS6&lid=LSTSPYFT28C83GYFSS6DR5LHK&marketplace=FLIPKART&srno=s_1_16&otracker=search&otracker1=search&fm=organic&iid=dbae980a-bdad-46b8-a63c-4917774c4c14.SPYFT28C83GYFSS6.SEARCH&ppt=sp&ppn=sp&ssid=muxfiknilc0000001599816814005&qH=18cad6cea86262ae',
		'https://www.flipkart.com/asian-paints-ezycr8-diy-aerosol-spray-crackle-glass-200-ml-brown-spray-paint/p/itm960aa6a9aea19?pid=SPYFT28CB74VAUMW&lid=LSTSPYFT28CB74VAUMWS78PZY&marketplace=FLIPKART&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=49c38fd4-b4ed-498d-ad6e-496814eede5e.SPYFT28CB74VAUMW.SEARCH&ppt=sp&ppn=sp&ssid=2c9jq9tkg00000001599819326634&qH=d791816e2523b217',
		'https://www.flipkart.com/asian-paints-ezycr8-trucare-diy-self-painting-kit-roller-brush-tray-sponge-masking-tape-1057sr68122-paint-roller/p/itm223ce6203b0b7?pid=PTEFT27VWRCQDTAF&lid=LSTPTEFT27VWRCQDTAFDSWQTW&marketplace=FLIPKART&srno=s_1_4&otracker=search&otracker1=search&fm=SEARCH&iid=49c38fd4-b4ed-498d-ad6e-496814eede5e.PTEFT27VWRCQDTAF.SEARCH&ppt=sp&ppn=sp&ssid=2c9jq9tkg00000001599819326634&qH=d791816e2523b217',
		'https://www.flipkart.com/asian-paints-ezycr8-diy-aerosol-spray-frosted-glass-200-ml-clear-spray-paint/p/itm3447c0f6e0685?pid=SPYFT28CB5WZ3U6N&lid=LSTSPYFT28CB5WZ3U6NAXTPCE&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=dbae980a-bdad-46b8-a63c-4917774c4c14.SPYFT28CB5WZ3U6N.SEARCH&ppt=sp&ppn=sp&ssid=muxfiknilc0000001599816814005&qH=18cad6cea86262ae'
		]

def main():
	reviews = []
	for url in urls:
		try:
			prod_rev = Scraper.get_reviews(url)	# Scraping reviews for this url
			reviews+=prod_rev
		except:
			print("Not completed for: " +url)
			continue
	scores = Analysis.analyze(reviews, wordcloud=True, file_path='another\\temp.png')	# Analyzing scraped reviews
	print(f'\nNegative {scores["neg"]:.2f}% Neutral {scores["neu"]:.2f}% Positive {scores["pos"]:.2f}%')

	#url = input("Enter a Flipkart or Amazon product URL to analyze: \n")	
	#reviews = Scraper.get_reviews(url)	# Scraping reviews for this url
	scores = Analysis.analyze(reviews, wordcloud=False, file_path='another\\temp.png')	# Analyzing scraped reviews
	print(f'\nNegative {scores["neg"]:.2f}%, Neutral {scores["neu"]:.2f}%, Positive {scores["pos"]:.2f}%')

if __name__ == '__main__':
	main()
