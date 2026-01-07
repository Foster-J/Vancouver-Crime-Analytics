CREATE INDEX IF NOT EXISTS index_crime_datetime ON crime_incidents(incident_datetime);
CREATE INDEX IF NOT EXISTS index_crime_date ON crime_incidents(incident_date);
CREATE INDEX IF NOT EXISTS index_crime_neighbourhood ON crime_incidents(neighbourhood);
CREATE INDEX IF NOT EXISTS index_crime_type ON crime_incidents(crime_type);
CREATE INDEX IF NOT EXISTS index_crime_category ON crime_incidents(crime_category);
CREATE INDEX IF NOT EXISTS index_crime_year_month ON crime_incidents(year, month);
