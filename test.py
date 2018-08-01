import json
import requests
import time

def main():
  success = 0
  companies = ["Gordon Ramsay Group", "Edwardian Hotels London", "Como Hotels & Resorts", "The Langham, London", "Delamina EAST", "Marks Club", "The Change Group", "Firmdale Hotels Plc", "Onodera", "The Wellesley", "Duck&waffle", "Bluebird White City", "Hakkasan Ltd.", "Edwardian Hotels London", "The Garrison", "PPHE Accommodation Services", "Claibon Property Services Ltd", "Property Management Recruitment (PMR)", "Park Plaza Westminster Bridge", "Renaissance London Heathrow", "CV- Library", "Evolve Hospitality", "Flying Butler apartments LTD", "WGC Ltd", "The Lanesborough", "Unite Students", "11 Cadogan Gardens", "HC-One Limited", "Care First UK Recruitment Solutions", "Cook", "Kafe 1788 ltd", "Red Lion", "Bright Horizons", "Ray Associates", "Pimlico", "1920 bar", "Souli", "Dose", "The Volunteer", "Purley Sports Club", "Care First UK Recruitment Solutions", "Pinocchio's", "Little Learners Day Nursery", "Abbatt Property Services", "FirstPort Property Services", "Abbatt Property Services", "Randstad CPE", "Guoman - The Tower Hotel", "ABBATT GROUP", "Randstad CPE", "A2Dominion", "Property Management Recruitment", "Chester James Consulting Limited", "FirstPort", "Arora Hotels Limited", "BBL Recruitment", "ABBATT GROUP", "Alexander Ash", "Forsyth Barnes Limited", "BWSR", "Best Recruit", "Citifocus Limited", "XPO Logistics", "Y H A ENGLAND & WALES LTD", "2M Employment Solutions Ltd", "Telegraph Jobs", "Rise Technical Recruitment Limited", "love recruitment limited", "KPMG UK", "Royal Mail Group", "The SmartList", "Driver Hire", "International Career Master", "Kemp Recruitment Limited", "WPRG LTD", "Staffing Match - Transport", "Service Care Solutions", "Construction People Limited", "Driver Hire", "Axiom Personnel Ltd", "Headstart Employment.", "Optimum All Drive Limited"]
  print('Companies: '+ str(len(companies)) + '\n\n')

  for company in companies:
    response = requests.post('http://biggui.pythonanywhere.com/postcode', data = {'company':company, 'city': 'London'})

    print(company)
    print(response.text)

    if json.loads(response.text)['data'] != None:
      success += 1

    time.sleep(10)

  print('Success: '+str(success/len(companies) * 100)+'%')

  return

if __name__ == "__main__":
    main()
