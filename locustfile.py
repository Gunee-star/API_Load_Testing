from locust import HttpUser, TaskSet, task, between, constant
# from locust import ResponseError
from SalonListing import listing_filters, host_listing, host_listing_management, get_list_dates, get_home_notice, get_hosting_preference, get_home_listing, get_listing_hours, get_listing_images, get_listing_insurance_preference, get_listing_price, get_rental_type
import json
import requests
headers = {"Content-Type": 'application/json',
           "X-Authorization": '4533f5d99715640dc4adb37289a8bd850f3f4eff'}


class AuthUser(HttpUser):
    min_wait = 1000
    max_wait = 1000

#  Auth Controller API'S for Load Testing
    # @task(1)
    # def get_user_reservation_profile(self):
    #     a = self.client.get(
    #         '/api/v4/Auth/get-user-reservation-profile', name="User Reservation Profile", headers=headers)
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    # @task(1)
    # def check_email_signup(self):
    #     a = self.client.get(
    #         "/api/v4/Auth/check-email-signup?email=guneet@shearshare.com", name="Email Verification",)
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    # @task(1)
    # def get_user_details(self):
    #     a = self.client.get("/api/v4/Auth/get-user-details",
    #                         name="User Details", headers=headers)
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    # @task(1)
    # def logout(self):
    #     a = self.client.post("/api/v4/Auth/logout", name="Logout", headers=headers, json={
    #         "deviceId": "string"
    #     })
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

# Coupon Controller API's Load Testing
    # @task(1)
    # def coupon(self):
    #     a = self.client.get(
    #         "/api/v4/Coupon/apply-coupon?Rate=50&ListingId=353&UserId=169&CouponCode=CHIRAG1", name="Apply Coupon", headers=headers)
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    # @task(1)
    # def get_stylist_inbox(self):
    #     a = self.client.get("/api/v4/Chat/get-stylist-inbox",
    #                         name="Stylist Inbox", headers=headers)
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    # @task(1)
    # def test_bugReport(self):
    #     a = self.client.post("/api/v4/BugReport/report-bug", name="Report Bug", headers=headers, json={
    #         "bug": "API Testing"
    #     })
    #     if a.status_code == 200:
    #         pass
    #     else:
    #         if a.status_code >= 400 and a.status_code <= 405:
    #             raise AssertionError("API Hit Failing: "+str(a.status_code))
    #         if a.status_code == 500:
    #             raise AssertionError(
    #                 "Internal Server Error: "+str(a.status_code))

    @task(1)
    def test_listig(self):
        listing_filters(self)
        host_listing(self)
        host_listing_management(self)
        get_list_dates(self)
        get_home_listing(self)
        get_home_notice(self)
        get_hosting_preference(self)
        get_listing_hours(self)
        get_listing_images(self)
        get_listing_insurance_preference(self)
        get_listing_price(self)
        get_rental_type(self)
