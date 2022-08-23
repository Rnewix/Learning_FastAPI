
#Python
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field, EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Path

app= FastAPI()

						 	
class Grade_Univ(Enum):							
    primer_grado = 'primer grado'									
    segundo_grado = 'segundo grado'
    tercer_grado = 'tercer grado'

class Student(BaseModel):
	student_id: int = Field(..., gt=0, le= 1000000) #, title= "Studen ID", description= "This ID is Unique for every student"
	apellido_paterno: str = Field(..., min_length=1, max_length=15)
	apellido_materno: str = Field(..., min_length=1, max_length=15)
	nombres: str = Field(..., min_length=1, max_length=20)
	grado_universitario: Grade_Univ = Field(...)
	calificacion_ingreso: float = Field(..., gt=60.00, le= 100.00)
	#email: EmailStr = Field(..., max_length=50)
	hobby: str = Field(default = None, max_length=30)	
	
	class Config:								
		schema_extra = {
                "example" : {
                    "student_id": 666,	
				    "apellido_paterno": "Roca", 
				    "apellido_materno": "Dono", 
				    "nombres": "Carlos", 
                    "grado_universitario": "tercer grado", 
                    "calificacion_ingreso": 97.55, 
                    #"email": "roca@gmail.com"
                    }
			    }

@app.get("/")									
async def root():								
    return {"message": "Hello World"}				

@app.get("/URL/estudiantes/{student_id}")
async def get_student(
	student_id: int = Path (...)
	):
	return {"message": "The student is..."}

@app.post("/URL/new_student")
def create_student(
	student: Student = Body(...)
	):
	return student