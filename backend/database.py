
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
            "experienceLevel": "experienced buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["single", "luxury"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["enthusiastic", "reserved", "attentive"]
        },
        {
            "firstName": "arshia",
            "lastName": "aravinthan",
            "email": "aravinat@gmail.com",
            "phone": "7263728039",
            "city": "dallas",
            "state": "texas",
            "experienceLevel": "experienced buyer",
            "timeline": "future (12+)",
            "pronouns": "he/him",
            "language": "spanish",
            "propertyType": ["single", "luxury"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["enthusiastic", "reserved", "people-oriented"]
        },
        {
            "firstName": "olivia",
            "lastName": "clark",
            "email": "olivia.clark@gmail.com",
            "phone": "2135647890",
            "city": "miami",
            "state": "florida",
            "experienceLevel": "first-time buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "single"],
            "lifestyle": ["urban", "near schools and parks", "commute-friendly"],
            "personality": ["attentive", "empathetic", "adaptable"]
        }
    ],
    "clients": [
        {
            "firstName": "bob",
            "lastName": "the builder",
            "email": "bob@gmail.com",
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
            "pronouns": "she/her" ,
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
            "city": "sunnyvale",
            "state": "california",
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
            "city": "los angeles",
            "state": "california",
            "budget": "700000",
            "experienceLevel": "experienced buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["condo", "multi"],
            "lifestyle": ["urban", "near schools and parks", "near shopping and dining"],
            "personality": ["knowlegeable", "adaptable", "people-oriented"]
        },
        {
            "firstName": "lucas",
            "lastName": "brown",
            "email": "lucas.brown@email.com",
            "phone": "6171234567",
            "city": "boston",
            "state": "massachusetts",
            "budget": "400000",
            "experienceLevel": "first-time buyer",
            "timeline": "no timeline",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["single", "townhouse", "condo"],
            "lifestyle": ["suburban", "pet-friendly", "commute-friendly"],
            "personality": ["reserved", "attentive", "empathetic"]
        },
        {
            "firstName": "olivia",
            "lastName": "johnson",
            "email": "olivia.johnson@email.com",
            "phone": "2125553456",
            "city": "new york",
            "state": "new york",
            "budget": "600000",
            "experienceLevel": "experienced buyer",
            "timeline": "immediate (0-3m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "luxury"],
            "lifestyle": ["urban", "near shopping and dining", "commute-friendly"],
            "personality": ["enthusiastic", "attentive", "knowledgeable"]
        },
        {
            "firstName": "zoe",
            "lastName": "cooper",
            "email": "zoe.cooper@gmail.com",
            "phone": "3121234567",
            "city": "bakersfield",
            "state": "california",
            "budget": "600000",
            "experienceLevel": "first-time buyer",
            "timeline": "medium-long (3-12m)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "townhouse"],
            "lifestyle": ["urban", "commute-friendly", "near shopping and dining"],
            "personality": ["reserved", "attentive", "empathetic"]
        },
        {
            "firstName": "emma",
            "lastName": "williams",
            "email": "emma.williams@email.com",
            "phone": "2025550199",
            "city": "washington",
            "state": "district of columbia",
            "budget": "500000",
            "experienceLevel": "first-time buyer",
            "timeline": "future (12+)",
            "pronouns": "she/her",
            "language": "english",
            "propertyType": ["condo", "townhouse"],
            "lifestyle": ["urban", "near shopping and dining", "commute-friendly"],
            "personality": ["enthusiastic", "people-oriented", "reserved"]
        },
        {
            "firstName": "joseph",
            "lastName": "watson",
            "email": "joseph.watson@gmail.com",
            "phone": "4152345678",
            "city": "san jose",
            "state": "california",
            "budget": "450000",
            "experienceLevel": "first-time buyer",
            "timeline": "future (12+)",
            "pronouns": "he/him",
            "language": "english",
            "propertyType": ["single", "luxury"],
            "lifestyle": ["suburban", "near schools and parks", "pet-friendly"],
            "personality": ["attentive", "enthusiastic", "empathetic"]
        },
        {
            "firstName": "sofia",
            "lastName": "carlos",
            "email": "sofia.carlos@gmail.com",
            "phone": "6502986527",
            "city": "chicago",
            "state": "illinois",
            "budget": "400000",
            "experienceLevel" : "investment properties",
            "timeline" : "immediate(0-3m)",
            "pronouns": "she/her" ,
            "language" : "english",
            "propertyType": ["luxury", "single", "multi", "condo", "townhouse"],
            "lifestyle" : ["urban", "suburban", "rural", "commute-friendly", "pet-friendly", "near shopping and dining"],
            "personality" : ["knowlegeable", "confrontational", "enthusiastic", "reserved", "empathetic", "attentive", "adaptable", "people-oriented"]

        }, 
    ],
}
