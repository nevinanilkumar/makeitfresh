district_labels = ['Thiruvananthapuram', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode', 'Wayanadu', 'Kannur', 'Kasaragod']

def get_districts():
    districts = []
    for district in district_labels[::-1]:
        districts.append((district.lower(), district))
    return districts
