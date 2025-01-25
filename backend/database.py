print("kdjfs,")
db = {
    "realtors": [
        {
            "firstName": "howard",
            "lastName": "gillman",
            "email": "howard_gillman@gmail.com",

            "phone": "6502372986",
            "city": "irvine",
            "state": "california",

            #one answer
            #["first-time buyer", "experienced buyer", "investment properties"]
            "experienceLevel" : "experienced buyer",
            #["immediate (0-3m)", "medium-long (3-12m)", "future (12+)", "no timeline"]
            "timeline" : "immediate(0-3m)",
            #["she/her", "he/him", "they/them"]
            "pronouns": "he/him" ,
            #["english", "spanish", "hindi", "arabic", "french"]
            "language" : "english",

            #multiple answers
            "propertyType": ["luxury", "single", "multi", "condo", "townhouse", "apartment"],
            "lifestyle" : ["urban", "suburban", "rural", "near schools and parks", "commute-friendly", "pet-friendly", "near shopping and dining"],

            #personality (max 3)
            "personality" : ["knowlegeable", "confrontational", "enthusiastic", "reserved", "empathetic", "attentive", "adaptable", "people-oriented"]

        }, 
        {
        "firstName": "michael",
        "lastName": "thomas",
        "email": "michael.thomas@gmail.com",
        "phone": "3216549870",
        "city": "chicago",
        "state": "illinois",
        "budget": "650000",
        "experienceLevel": "experienced buyer",
        "timeline": "immediate (0-3m)",
        "pronouns": "he/him",
        "language": "english",
        "propertyType": ["single", "luxury"],
        "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
        "personality": ["enthusiastic", "reserved", "attentive"]
    },
    {
        "firstName": "olivia",
        "lastName": "clark",
        "email": "olivia.clark@gmail.com",
        "phone": "2135647890",
        "city": "miami",
        "state": "florida",
        "budget": "500000",
        "experienceLevel": "first-time buyer",
        "timeline": "medium-long (3-12m)",
        "pronouns": "she/her",
        "language": "english",
        "propertyType": ["condo", "single"],
        "lifestyle": ["urban", "near schools and parks", "commute-friendly"],
        "personality": ["attentive", "empathetic", "adaptable"]
    },
    {
        "firstName": "james",
        "lastName": "martin",
        "email": "james.martin@gmail.com",
        "phone": "3129876543",
        "city": "chicago",
        "state": "illinois",
        "budget": "750000",
        "experienceLevel": "investment properties",
        "timeline": "future (12+)",
        "pronouns": "he/him",
        "language": "english",
        "propertyType": ["multi", "luxury"],
        "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
        "personality": ["knowlegeable", "attentive", "people-oriented"]
    },
    {
        "firstName": "ella",
        "lastName": "miller",
        "email": "ella.miller@gmail.com",
        "phone": "6154329876",
        "city": "nashville",
        "state": "tennessee",
        "budget": "550000",
        "experienceLevel": "first-time buyer",
        "timeline": "immediate (0-3m)",
        "pronouns": "she/her",
        "language": "english",
        "propertyType": ["single", "townhouse"],
        "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
        "personality": ["attentive", "empathetic", "enthusiastic"]
    },
    {
        "firstName": "benjamin",
        "lastName": "davis",
        "email": "benjamin.davis@gmail.com",
        "phone": "6172345678",
        "city": "boston",
        "state": "massachusetts",
        "budget": "800000",
        "experienceLevel": "experienced buyer",
        "timeline": "medium-long (3-12m)",
        "pronouns": "he/him",
        "language": "english",
        "propertyType": ["luxury", "single"],
        "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
        "personality": ["enthusiastic", "adaptable", "reserved"]
    },
    {
        "firstName": "sophie",
        "lastName": "evans",
        "email": "sophie.evans@gmail.com",
        "phone": "7341230987",
        "city": "ann arbor",
        "state": "michigan",
        "budget": "400000",
        "experienceLevel": "first-time buyer",
        "timeline": "medium-long (3-12m)",
        "pronouns": "she/her",
        "language": "english",
        "propertyType": ["condo", "townhouse"],
        "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
        "personality": ["reserved", "attentive", "empathetic"]
    },
    {
        "firstName": "liam",
        "lastName": "wilson",
        "email": "liam.wilson@gmail.com",
        "phone": "4046543210",
        "city": "atlanta",
        "state": "georgia",
        "budget": "600000",
        "experienceLevel": "first-time buyer",
        "timeline": "immediate (0-3m)",
        "pronouns": "he/him",
        "language": "english",
        "propertyType": ["single", "luxury"],
        "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
        "personality": ["enthusiastic", "reserved", "attentive"]
    },
    {
        "firstName": "harper",
        "lastName": "adams",
        "email": "harper.adams@gmail.com",
        "phone": "2023456789",
        "city": "washington",
        "state": "district of columbia",
        "budget": "950000",
        "experienceLevel": "experienced buyer",
        "timeline": "future (12+)",
        "pronouns": "she/her",
        "language": "english",
        "propertyType": ["multi", "luxury"],
        "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
        "personality": ["knowlegeable", "attentive", "people-oriented"]
    },
    {
        "firstName": "jackson",
        "lastName": "moore",
        "email": "jackson.moore@gmail.com",
        "phone": "6159876543",
        "city": "knoxville",
        "state": "tennessee",
        "budget": "700000",
        "experienceLevel": "investment properties",
        "timeline": "medium-long (3-12m)",
        "pronouns": "he/him",
        "language": "english",
        "propertyType": ["single", "luxury"],
        "lifestyle": ["suburban", "pet-friendly", "near schools and parks"],
        "personality": ["enthusiastic", "adaptable", "attentive"]
    },
    {
        "firstName": "zoe",
        "lastName": "harris",
        "email": "zoe.harris@gmail.com",
        "phone": "9196549876",
        "city": "raleigh",
        "state": "north carolina",
        "budget": "550000",
        "experienceLevel": "first-time buyer",
        "timeline": "immediate (0-3m)",
        "pronouns": "she/her",
        "language": "english",
        "propertyType": ["townhouse", "condo"],
        "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
        "personality": ["reserved", "empathetic", "people-oriented"]
    }

        

        
        

    ],
    "clients": [
        {
            "firstName": "ira",
            "lastName": "dharia",
            "email": "ira@gmail.com",
            "phone": "6502372787",
            "city": "pleasanton",
            "state": "california",

            "budget": "400000",

             #one answer
            #["first-time buyer", "experienced buyer", "investment properties"]
            "experienceLevel" : "experienced buyer",
            #["immediate (0-3m)", "medium-long (3-12m)", "future (12+)", "no timeline"]
            "timeline" : "immediate(0-3m)",
            #["she/her", "he/him", "they/them"]
            "pronouns": "he/him" ,
            #["english", "spanish", "hindi", "arabic", "french"]
            "language" : "english",

            #multiple answers
            "propertyType": ["luxury", "single", "multi", "condo", "townhouse"],
            "lifestyle" : ["urban", "suburban", "rural", "near schools and parks", "commute-friendly", "pet-friendly", "near shopping and dining"],

            #personality (max 3)
            "personality" : ["knowlegeable", "confrontational", "enthusiastic", "reserved", "empathetic", "attentive", "adaptable", "people-oriented"]

        }, 
        
        {
            "firstName": "emily",
            "lastName": "davis",
            "email": "emily.davis@gmail.com",
            "phone": "6123456789",
            "city": "minneapolis",
            "state": "minnesota",
            "budget": "500000",
            "experienceLevel": "first-time buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["single", "townhouse"],
            "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
            "personality": ["enthusiastic", "attentive", "empathetic"]
        },
        {
            "firstName": "omar",
            "lastName": "alvarez",
            "email": "omar.alvarez@gmail.com",
            "phone": "3059876543",
            "city": "miami",
            "state": "florida",
            "budget": "700000",
            "experienceLevel": "experienced buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "he/him",
            "language": "spanish",
            "propertyType": ["luxury", "multi"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["knowlegeable", "adaptable", "people-oriented"]
        },
        {
            "firstName": "zoe",
            "lastName": "cooper",
            "email": "zoe.cooper@gmail.com",
            "phone": "3121234567",
            "city": "chicago",
            "state": "illinois",
            "budget": "600000",
            "experienceLevel": "first-time buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "townhouse"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["reserved", "attentive", "empathetic"]
        },
        {
            "firstName": "joseph",
            "lastName": "watson",
            "email": "joseph.watson@gmail.com",
            "phone": "4152345678",
            "city": "portland",
            "state": "oregon",
            "budget": "450000",
            "experienceLevel": "first-time buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["single", "luxury"],
            "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
            "personality": ["attentive", "enthusiastic", "empathetic"]
        },
        {
            "firstName": "aria",
            "lastName": "johnson",
            "email": "aria.johnson@gmail.com",
            "phone": "3171239876",
            "city": "indianapolis",
            "state": "indiana",
            "budget": "550000",
            "experienceLevel": "experienced buyer",
            "timeline": "future (12+)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["luxury", "single"],
            "lifestyle": ["urban", "near shopping and dining", "commute-friendly"],
            "personality": ["knowlegeable", "reserved", "adaptable"]
        },
        {
            "firstName": "david",
            "lastName": "miller",
            "email": "david.miller@gmail.com",
            "phone": "7023456789",
            "city": "las vegas",
            "state": "nevada",
            "budget": "650000",
            "experienceLevel": "first-time buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["single", "townhouse"],
            "lifestyle": ["suburban", "pet-friendly", "near schools and parks"],
            "personality": ["enthusiastic", "people-oriented", "attentive"]
        },
        {
            "firstName": "nina",
            "lastName": "brown",
            "email": "nina.brown@gmail.com",
            "phone": "6142345678",
            "city": "columbus",
            "state": "ohio",
            "budget": "400000",
            "experienceLevel": "first-time buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "single"],
            "lifestyle": ["suburban", "pet-friendly", "near shopping and dining"],
            "personality": ["attentive", "empathetic", "enthusiastic"]
        },
        {
            "firstName": "juan",
            "lastName": "garcia",
            "email": "juan.garcia@gmail.com",
            "phone": "2141239876",
            "city": "dallas",
            "state": "texas",
            "budget": "750000",
            "experienceLevel": "experienced buyer",
            "timeline": "future (12+)",
            "pronouns": "he/him",
            "language": "spanish",
            "propertyType": ["luxury", "multi"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["knowlegeable", "attentive", "people-oriented"]
        },
        {
            "firstName": "samantha",
            "lastName": "lee",
            "email": "samantha.lee@gmail.com",
            "phone": "6262345678",
            "city": "seattle",
            "state": "washington",
            "budget": "600000",
            "experienceLevel": "first-time buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["luxury", "single"],
            "lifestyle": ["urban", "near shopping and dining", "commute-friendly"],
            "personality": ["enthusiastic", "attentive", "reserved"]
        },
        {
            "firstName": "andrew",
            "lastName": "wilson",
            "email": "andrew.wilson@gmail.com",
            "phone": "5202349876",
            "city": "tucson",
            "state": "arizona",
            "budget": "500000",
            "experienceLevel": "first-time buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["condo", "single"],
            "lifestyle": ["suburban", "pet-friendly", "near schools and parks"],
            "personality": ["empathetic", "attentive", "reserved"]
        }



    ],
}
