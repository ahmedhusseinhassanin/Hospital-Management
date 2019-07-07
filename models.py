from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Hospital_Information(models.Model):
    _name = 'hospital.information'
    name = fields.Char(required=True,string="Hospital Name")
    Type=fields.Selection([

                ('G','Governmental'),
                ('S','Special'),

            ],default='G')
    image=fields.Binary()
    website=fields.Char()
    phone=fields.Char()
    mobile=fields.Char()
    fax=fields.Char()
    email=fields.Char()
    description=fields.Text()
    address=fields.Char()
    street=fields.Char()
    city=fields.Selection([
        ('F','Fayoum'),
        ('C','Cairo'),
        ('P','Port Said'),
        ('T','Tanta')

    ] ,default='F')
    extra_information=fields.Html()

class Hospital_Building(models.Model):
    _name = 'hospital.building'
    name=fields.Char(required=True,string="Building Name")
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    floors=fields.Integer()
    code=fields.Char()
    mobile=fields.Char()
    extra_information=fields.Html()

class Rooms(models.Model):
    _name = 'hospital.rooms'
    name=fields.Char(string="Room Name",required=True)
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    building_name=fields.Many2one('hospital.building',ondelete='set null',string="Building Name",index=True)  
    floor_number=fields.Integer()
    beds_number=fields.Integer()
    extra_information=fields.Html()



class Operations_Rooms(models.Model):
    _name = 'operation.rooms'
    name=fields.Char(string="Room Name" ,required=True)
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    building_name=fields.Many2one('hospital.building',ondelete='set null',string="Building Name",index=True)  
    extra_information=fields.Html()

class Beds(models.Model):
    _name = 'hospital.beds'
    name=fields.Char(string="Bed Name",required=True)
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    building_name=fields.Many2one('hospital.building',ondelete='set null',string="Building Name",index=True) 
    room_name=fields.Many2one('hospital.rooms',ondelete='set null',string="Room Name",index=True)  
    phone=fields.Char()
    price=fields.Float()
    extra_information=fields.Html()

class Test_information(models.Model):
    _name = 'hospital.test'
    name=fields.Char(string="Lab Name",required=True)
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    building_name=fields.Many2one('hospital.building',ondelete='set null',string="Building Name",index=True) 
    floor_number=fields.Integer()  
    devices=fields.Text()
    extra_information=fields.Html()

class Test_available(models.Model):
    _name = 'hospital.tests'
    name=fields.Char(string="Name Of Test ",required=True)
    normal_range=fields.Float()
    test_price=fields.Float()
    extra_information=fields.Html()

class Test_reservation(models.Model):
    _name = 'test.reservation'
    name=fields.Char()
    age=fields.Float()
    city=fields.Char()
    gender=fields.Selection([
        ('M','Male'),
        ('F','Female')
    ])
    phone=fields.Char()
    Type=fields.Many2one('hospital.tests',string='Type of Test',ondelete='set null',index=True)
    price=fields.Float()
    extra_information=fields.Html(string=" Patient history For Test Lab ")

# to add types of Images and it,s information

class Image_information(models.Model):
    _name = 'image.information'
    name=fields.Char(string="Lab Name",required=True)
    hospital_name=fields.Many2one('hospital.information',ondelete='set null',string="Hospital Name",index=True)
    building_name=fields.Many2one('hospital.building',ondelete='set null',string="Building Name",index=True) 
    floor_number=fields.Integer()  
    devices=fields.Text()
    extra_information=fields.Html(string=" Patient Images History ")


class Image_available(models.Model):
    _name = 'image.available'
    name=fields.Char(string="The Type Of Image ",required=True)
    image_price=fields.Float()
    extra_information=fields.Html()
    

class Image_reservation(models.Model):
    _name = 'image.reservation'
    name=fields.Char()
    age=fields.Float()
    city=fields.Char()
    gender=fields.Selection([
        ('M','Male'),
        ('F','Female')
    ])
    phone=fields.Char()
    Type=fields.Many2one('hospital.tests',string='Type of Test',ondelete='set null',index=True)
    price=fields.Float()
    extra_information=fields.Html(string=" Patient History Images")

    
