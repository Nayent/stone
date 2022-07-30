class Bill:
    def __init__(self, email_list, shopping_list):
        self.email_list = email_list
        self.shopping_list = shopping_list

    def delete_duplicate_emails(self):
        # Delete duplicates and NULL values
        return list(filter(None, set(self.email_list)))

    def validate_duplicate_email(self):
        # Only return if has or not duplicate emails
        if len(self.email_list) != len(set(self.email_list)):
            raise Exception("The list has duplicate emails!")
        return True

    def validate_duplicate_email_v2(self):
        # Return error with first duplicate email
        if len(self.email_list) != len(set(self.email_list)):
            unique_email = set()
            for email in self.email_list:
                if email in unique_email:
                    raise Exception(f"The email {email} is duplicated!")
                unique_email.add(email)
        return True

    def validate_duplicate_email_v3(self):
        # Return error with all duplicate email
        if len(self.email_list) != len(set(self.email_list)):
            unique_email = set()
            duplicate_emails = {}
            for email in self.email_list:
                if email in unique_email:
                    if email in duplicate_emails:
                        duplicate_emails[email] += 1
                    else:
                        duplicate_emails[email] = 1
                unique_email.add(email)
            for email, count in duplicate_emails.items():
                print(f"The email {email} has {count} duplicates!")
            return False
        return True

    def validate_empty_list(self):
        # Return the empty list
        iter_dict = {
            'email': self.email_list,
            'shopping': self.shopping_list,
        }
        for name, list in iter_dict.items():
            if not list:
                raise Exception(f"Empty {name} List!")
        return True

    def validate_qnt_price(self):
        # Return the item that has negative value
        for item, info in self.shopping_list.items():
            if info['quantity'] < 0 or info['price'] < 0:
                raise Exception(f"The item '{item}' has negative value!")
        return True

    def price_all_items(self):
        # Return total price
        full_price = 0
        for info in self.shopping_list.values():
            full_price += info['quantity'] * info['price']
        return full_price
    
    def split_bill(self):
        # Return a dict with email as the key and the amount he needs to pay
        amount_email = {}
        aux = 1
        remainder = self.amount % len(self.email_list)
        entire = self.amount // len(self.email_list)
        for email in self.email_list:
            if remainder > 0:
                remainder -= 1
            else:
                aux = 0
            amount_email[email] = entire + aux

        return amount_email
    
    def split(self):
        # Main function
        self.validate_duplicate_email()
        self.validate_empty_list()
        self.validate_qnt_price()
        self.amount = self.price_all_items()
        return self.split_bill()