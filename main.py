from requests import get

def get_ip():
    return get('https://api64.ipify.org?format=json').json().get("ip")

def get_location():
    ip_address = get_ip()
    response = get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "network" : response.get("org")
    }
    return location_data

print(get_location())