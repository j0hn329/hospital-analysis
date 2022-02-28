import sqlite3

conn = sqlite3.connect("Hospital.db")
c = conn.cursor()

class hospital:
    def __init__(self, providerid):
        self.providerid = providerid

    def display_hospital_info(self):
        c.execute('''SELECT provider_id, hospital_name, city, state, county,
                        type, ownership, rating
                    FROM hospital_info WHERE provider_id=:providerid''',
                        {'providerid': self.providerid})
        hos_info = c.fetchall()
        return hos_info

    def add_hospital(self):
        hos_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM hospital_info WHERE provider_id=:hos_id',
                     {'hos_id': hos_id})
        fetch_id = c.fetchone()

        if fetch_id != None:
            print('Hospital with id:', hos_id, "already exists")
        else:
            hos_name = input("Enter hospital name: ")
            hos_city = input("Enter hospital city: ")
            hos_state = input("Enter hospital state: ")
            hos_county = input("Enter hospital county: ")
            hos_type = input("Enter hospital type: ")
            hos_owner = input("Enter hospital owner: ")
            hos_rating = input("Enter hospital rating: ")

            c.execute('''INSERT INTO hospital_info(provider_id, hospital_name,
                city, state, county,
                type, ownership, rating)
                VALUES(?,?,?,?,?,?,?,?)''', (hos_id, hos_name, hos_city, hos_state,
                hos_county, hos_type, hos_owner, hos_rating))
            conn.commit()

    def remove_hospital(self):
        hos_id = input("Enter hospital provider id: ")

        c.execute('SELECT provider_id FROM hospital_info WHERE provider_id=:hos_id',
                     {'hos_id': hos_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital information cannot be removed as it does not exist')
        else:
            c.execute('DELETE FROM hospital_info WHERE provider_id=:hos_id',
                     {'hos_id': hos_id})
            print("Hospital information sucessfully removed")
        conn.commit()

    def update_hospital_rating(self):
        hos_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM hospital_info WHERE provider_id=:hos_id',
                     {'hos_id': hos_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital with id:', hos_id, "doesn't exist")
        else:
            hos_rating = input("Enter new hospital rating: ")

            c.execute('UPDATE hospital_info SET rating=? WHERE provider_id=?',
                        (hos_rating, hos_id))
            conn.commit()
            print("Hospital rating sucessfully updated")

class reviews(hospital):
    def __init__(self, hospit):
        self.providerid = hospit.providerid

    def display_reviews(self):
        c.execute('''SELECT provider_id, number_of_reviews, last_review, reviews_per_month
            FROM reviews WHERE provider_id=:providerid''',
                {'providerid': self.providerid})
        rev_info = c.fetchall()
        return rev_info

    def add_review(self):
        rev_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM reviews WHERE provider_id=:rev_id',
                     {'rev_id': rev_id})
        fetch_id = c.fetchone()

        if fetch_id != None:
            print('Hospital with id:', rev_id, "already exists")
        else:
            rev_num_reviews = input("Enter number of hospital reviews: ")
            rev_last_review = input("Enter last hospital review: ")
            rev_per_month = input("Enter hospital reviews per month: ")

            c.execute('''INSERT INTO reviews(provider_id, number_of_reviews,
                last_review, reviews_per_month)
                VALUES(?,?,?,?)''', (rev_id, rev_num_reviews, rev_last_review, rev_per_month))
            conn.commit()

    def remove_review(self):
        rev_id = input("Enter hospital provider id: ")

        c.execute('SELECT provider_id FROM reviews WHERE provider_id=:rev_id',
                     {'rev_id': rev_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital reviews cannot be removed as it does not exist')
        else:
            c.execute('DELETE FROM reviews WHERE provider_id=:rev_id',
                     {'rev_id': rev_id})
            print("Hospital reviews sucessfully removed")
        conn.commit()

    def update_reviews(self):
        rev_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM reviews WHERE provider_id=:rev_id',
                     {'rev_id': rev_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital with id:', rev_id, "doesn't exist")
        else:
            rev_num_reviews = input("Enter number of hospital reviews: ")
            rev_last_review = input("Enter last hospital review: ")
            rev_per_month = input("Enter hospital reviews per month: ")

            c.execute('''UPDATE reviews
                        SET number_of_reviews=?, last_review=?, reviews_per_month=?
                        WHERE provider_id=?''',
                        (rev_num_reviews, rev_last_review, rev_per_month, rev_id))
            conn.commit()
            print("Hospital reviews sucessfully updated")

class quality_of_care(hospital):
    def __init__(self, hospit):
        self.providerid = hospit.providerid

    def display_quality_of_care(self):
        c.execute('''SELECT provider_id,mortality_nat_comparison, safety_of_care_nat_comparison,
                    readmission_nat_comparison, patient_experience_nat_comparison,
                    effectiveness_of_care_nat_comparison, timeliness_of_care_nat_comparison,
                    efficient_imaging_nat_comparison
                FROM quality_of_care WHERE provider_id=:providerid''',
                {'providerid': self.providerid})
        qoc_info = c.fetchall()
        return qoc_info

    def add_qoc(self):
        qoc_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM quality_of_care WHERE provider_id=:qoc_id',
                     {'qoc_id': qoc_id})
        fetch_id = c.fetchone()

        if fetch_id != None:
            print('Hospital with id:', qoc_id, "already exists")
        else:
            qoc_mortality = input("Enter hospital mortaility national comparison: ")
            qoc_safety = input("Enter hospital safety national comparison: ")
            qoc_readmission = input("Enter hospital readmission national comparison: ")
            qoc_pat_exp = input("Enter hospital patient experience national comparison: ")
            qoc_eff_of_care = input("Enter hospital effectiveness of care national comparison: ")
            qoc_timeliness = input("Enter hospital timeliness national comparison: ")
            qoc_eff_img = input("Enter hospital efficient imaging national comparison: ")

            c.execute('''INSERT INTO quality_of_care(provider_id,mortality_nat_comparison,
                    safety_of_care_nat_comparison, readmission_nat_comparison,
                    patient_experience_nat_comparison, effectiveness_of_care_nat_comparison,
                    timeliness_of_care_nat_comparison, efficient_imaging_nat_comparison)
                VALUES(?,?,?,?,?,?,?,?)''', (qoc_id, qoc_mortality, qoc_safety, qoc_readmission,
               qoc_pat_exp, qoc_eff_of_care, qoc_timeliness, qoc_eff_img))
            print('Hospital quality of care with id:', qoc_id, "successfully added")
            conn.commit()

    def remove_qoc(self):
        qoc_id = input("Enter hospital provider id: ")

        c.execute('SELECT provider_id FROM quality_of_care WHERE provider_id=:qoc_id',
                     {'qoc_id': qoc_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital quality of care information cannot be removed as it does not exist')
        else:
            c.execute('DELETE FROM quality_of_care WHERE provider_id=:qoc_id',
                     {'qoc_id': qoc_id})
            print("Hospital quality of care information sucessfully removed")
        conn.commit()

    def update_qoc(self):
        qoc_id = input("Enter hospital provider id: ")
        c.execute('SELECT provider_id FROM quality_of_care WHERE provider_id=:qoc_id',
                     {'qoc_id': qoc_id})
        fetch_id = c.fetchone()

        if fetch_id == None:
            print('Hospital with id:', qoc_id, "doesn't exist")
        else:
            qoc_mortality = input("Enter new mortaility national comparison: ")
            qoc_safety = input("Enter new safety national comparison: ")
            qoc_readmission = input("Enter new readmission national comparison: ")
            qoc_pat_exp = input("Enter new patient experience national comparison: ")
            qoc_eff_of_care = input("Enter new effectiveness of care national comparison: ")
            qoc_timeliness = input("Enter new timeliness national comparison: ")
            qoc_eff_img = input("Enter new efficient imaging national comparison: ")

            c.execute('''UPDATE quality_of_care
                        SET mortality_nat_comparison=?, safety_of_care_nat_comparison=?,
                            readmission_nat_comparison=?, patient_experience_nat_comparison=?,
                            effectiveness_of_care_nat_comparison=?, timeliness_of_care_nat_comparison=?,
                            efficient_imaging_nat_comparison=?
                        WHERE provider_id=?''',
                        (qoc_mortality, qoc_safety, qoc_readmission, qoc_pat_exp, qoc_eff_of_care, qoc_timeliness, qoc_eff_img, qoc_id))
            conn.commit()
            print("Hospital quality of care sucessfully updated")

if __name__ == "__main__":

    hos = hospital(100)
    print(hos.display_hospital_info())
    #hos.add_hospital()
    #hos.remove_hospital()
    #hos.update_hospital_rating()

    rev = reviews(hos)
    print(rev.display_reviews())
    #rev.add_review()
    #rev.remove_review()
    #rev.update_reviews()

    qoc = quality_of_care(hos)
    print(qoc.display_quality_of_care())
    #qoc.add_qoc()
    #qoc.remove_qoc()
    #qoc.update_qoc()

import unittest

class testing(unittest.TestCase):

    def test_displaying_hospital(self):
        expected = [(10055, 'FLOWERS HOSPITAL', 'DOTHAN', 'AL', 'HOUSTON', 'Acute Care Hospitals', 'Proprietary', 4)]
        actual = hos.display_hospital_info()

        self.assertEqual(expected, actual)

    def test_displaying_reviews(self):
        expected = [(10055, 99, '24/08/2019', 1.28)]
        actual = rev.display_reviews()

        self.assertEqual(expected, actual)

    def test_displaying_qoc(self):
        expected = [(10055, 'Below the national average', 'Above the national average', 'Above the national average', 'Above the national average', 'Same as the national average', 'Above the national average', 'Same as the national average')]
        actual = qoc.display_quality_of_care()

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
