
#Python
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field, EmailStr

#FastAPI
from fastapi import FastAPI, status
from fastapi import Body, Path

app= FastAPI()

						 	
class Grade_Univ(Enum):							
    primer_grado = 'primer grado'									
    segundo_grado = 'segundo grado'
    tercer_grado = 'tercer grado'

class StudentBase(BaseModel):
	student_id: int = Field(..., gt=0, le= 1000000, title= "Studen ID", description= "This ID is Unique for every student") 
	apellido_paterno: str = Field(..., min_length=1, max_length=15)
	apellido_materno: str = Field(..., min_length=1, max_length=15)
	nombres: str = Field(..., min_length=1, max_length=20)
	grado_universitario: Grade_Univ = Field(...)
	hobby: str = Field(default = None, max_length=30)	
	
	class Config:								
		schema_extra = {
                "example" : {
                    "student_id": 666,	
				    "apellido_paterno": "Roca", 
				    "apellido_materno": "Dono", 
				    "nombres": "Carlos", 
                    "grado_universitario": "tercer grado"
                    }
			    }
class Student(StudentBase):
    edad: int = Field(..., gt=17)
    email: EmailStr = Field(..., max_length=50)
    calificacion_ingreso: float = Field(..., gt=60.00, le= 100.00)
    class Config: 
        schema_extra = {
                "example" : {
                    "edad": 21,
                    "calificacion_ingreso": 97.55, 
                    "email": "roca@gmail.com"
                    }
			    }
class Student_Output(StudentBase):
    pass

@app.get(
    path= "/", 
    status_code= status.HTTP_200_OK 
    )									
async def root():								
    return {"message": "Hello World"}				

@app.get(
    path= "/URL/estudiantes/{student_id}", 
    status_code= status.HTTP_202_ACCEPTED
    )
async def get_student(
	student_id: int = Path (...)
	):
	return {"message": "The student is..."}

@app.post(
    path= "/URL/new_student", 
    response_model = Student_Output, 
    status_code= status.HTTP_202_ACCEPTED)
def create_student(
	student: Student = Body(...)
	):
	return student