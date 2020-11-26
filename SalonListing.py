from locust import HttpUser, TaskSet, task, between, constant
from datetime import datetime
# from locust import ResponseError
import json
import requests
headers = {"Content-Type": 'application/json',
           "X-Authorization": '4533f5d99715640dc4adb37289a8bd850f3f4eff'}


def statusCode(self, a):
    if a.status_code == 200:
        pass
    else:
        if a.status_code >= 400 and a.status_code <= 405:
            raise AssertionError("API Hit Failing: "+str(a.status_code))
        if a.status_code == 500:
            raise AssertionError(
                "Internal Server Error: "+str(a.status_code))


def listing_filters(self):
    a = self.client.get("/api/v4/SalonListing/listing-filters",
                        name="Listing Filters", headers=headers)
    # data = json.loads(a.text)
    statusCode(self, a)


def host_listing(self):
    a = self.client.get("/api/v4.1/SalonListing/host-listing",
                        name="Host Listing", headers=headers)
    statusCode(self, a)


def host_listing_management(self):
    a = self.client.get("/api/v4/SalonListing/host-listing-management?ListingId=353",
                        name="Host Listing Management", headers=headers)
    statusCode(self, a)


def get_list_dates(self):
    given_date = datetime.today().date()
    first_day_of_month = given_date.replace(day=1)
    a = self.client.get("/api/v4/SalonListing/get-list-dates?ListingId=353&StartDate="+str(first_day_of_month)+"&EndDate="+str(given_date),
                        name="List Dates", headers=headers)
    statusCode(self, a)


def get_listing_price(self):
    a = self.client.get("/api/v4/SalonListing/get-listing-price?ListingId=353",
                        name="Listing Price", headers=headers)
    statusCode(self, a)


def get_listing_insurance_preference(self):
    a = self.client.get("/api/v4/SalonListing/get-listing-insurance-preference?ListingId=353",
                        name="Listing Insurance Preference", headers=headers)
    statusCode(self, a)


def get_listing_hours(self):
    a = self.client.get("/api/v4/SalonListing/get-listing-hours?ListingId=353",
                        name="Listing Hours", headers=headers)
    statusCode(self, a)


def get_listing_images(self):
    a = self.client.get("/api/v4/SalonListing/get-listing-images?ListingId=353",
                        name="Listing Images", headers=headers)
    statusCode(self, a)


def get_hosting_preference(self):
    a = self.client.get("/api/v4/SalonListing/get-hosting-preferences?ListingId=353",
                        name="Hosting Preference", headers=headers)
    statusCode(self, a)


def get_rental_type(self):
    a = self.client.get("/api/v4/SalonListing/get-rental-type?ListingId=353",
                        name="Rental Type", headers=headers)
    statusCode(self, a)


def listing(self):
    a = self.client.get("/api/v4/SalonListing/listing?Id=353",
                        name="Listing", headers=headers)
    statusCode(self, a)


def get_home_listing(self):
    a = self.client.get("/api/v4/SalonListing/get-home-listings?UserLatitude=0&UserLongitude=0",
                        name="Home Listing", headers=headers)
    statusCode(self, a)


def get_home_notice(self):
    a = self.client.get("/api/v4/SalonListing/get-home-notice",
                        name="Banner Message", headers=headers)
    statusCode(self, a)
