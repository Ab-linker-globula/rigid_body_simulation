import bpy
import mathutils
import bmesh 
from bpy.types import (
        Menu,
        Operator,
        )
import os
import sys
from bpy.types import Operator
from bpy.props import (
        IntProperty,
        FloatProperty,
        )

######_____INPUT__________########################        
#Shift+S = snap_cursor_to_center ---- if you will change anything in 3dview you must return cursor to center for correctly work of this script
#Pivot_center for rotation = 3D Cursor           
layers_up_Z =1 #number_of_monomers (layers up Z_axis, minimum = 2)      
repeat = 2 #number_of_repeatitions (how many times to run script)
len_of_linker = 1#number_of_residues_in_linker (minimum = 1, maximum = 7)  
path_to_output_file = "/home/r/Изображения/run_script/blend.txt" #create file blend.txt and write path to this file.txt in this string.
path_to_file_with_result = "/home/r/Изображения/run_script/result.txt"#create file result.txt and write path to this file.txt in this string. You will see result in this file.
############################################

layers = layers_up_Z-2    
name = ('0','Icosphere','Icosphere.001','Icosphere.002','Icosphere.003','Icosphere.004','Icosphere.005','Icosphere.006')
loc_x = ('0',38.5, 42, 45.5, 49, 52.5, 56, 59.5)
location_x = loc_x[len_of_linker]
target= name[len_of_linker]
print(target)
             
################____CURSOR____####################################
def get_override(area_type, region_type):
    for area in bpy.context.screen.areas: 
        if area.type == area_type:             
            for region in area.regions:                 
                if region.type == region_type:                    
                    override = {'area': area, 'region': region} 
                    return override
    #error message if the area or region wasn't found
    raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                        "\n Make sure it's open while executing script.")


#we need to override the context of our operator    
override = get_override( 'VIEW_3D', 'WINDOW' )
#rotate about the X-axis by 45 degrees

for index in range(repeat): 
  bpy.data.scenes["Scene"].frame_current = 1

#####################____RANDOM_GRAVITY____#####################
  bpy.context.scene.gravity[2] = mathutils.noise.random()
  

#######################____OBJECTS____##############################
#add_cube
  bpy.ops.mesh.primitive_cube_add(radius=1, location = (0.0, 0.0, 0.0))
  bpy.ops.transform.resize(value = (20.0, 11.0, 2.4 ))
  bpy.ops.object.transform_apply(location=False, rotation =False, scale = True)
  bpy.ops.rigidbody.objects_add(type = 'PASSIVE')
  bpy.context.object.rigid_body.collision_shape = 'BOX'

#add_first_sphere_of_linker_passive
  bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(21.75, 0.0, 0.0))
  bpy.ops.rigidbody.objects_add(type = 'PASSIVE')
  bpy.context.object.rigid_body.collision_shape = 'SPHERE'

#add_second_sphere_of_linker_active
  if len_of_linker == 2:
       
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere']

#add_third_sphere_of_linker_active
  if len_of_linker == 3:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere'] 
    
      
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target =   bpy.data.objects['Icosphere.001']

#add_fourth_sphere_of_linker_active
  if len_of_linker == 4:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere'] 
    
      
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target =   bpy.data.objects['Icosphere.001']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.002']

#add_fifth_sphere_of_linker_active
  if len_of_linker == 5:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere'] 
    
      
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target =   bpy.data.objects['Icosphere.001']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.002']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.003']

#add_sixth_sphere_of_linker_active
  if len_of_linker == 6:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere'] 
    
      
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target =   bpy.data.objects['Icosphere.001']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.002']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.003']
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.004']

#add_seventh_sphere_of_linker_active
  if len_of_linker == 7:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 0, size = 1.75, location=(25.25, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere'] 
    
      
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target =   bpy.data.objects['Icosphere.001']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.002']

    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.003']
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.004']
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Icosphere.005']
      
      
#add_GLOBULAR_DOMAIN
  bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=15.0,   location=(location_x, 0.0, 0.0))

  bpy.data.scenes["Scene"].frame_current = 150
  bpy.ops.anim.keyframe_insert_menu(type='Scaling')
  bpy.data.scenes["Scene"].frame_current = 1
  bpy.ops.transform.resize(value = (0.01, 0.01, 0.01 ))
  bpy.ops.anim.keyframe_insert_menu(type='Scaling')

  bpy.ops.group.create(name = 'globula')
  bpy.ops.object.group_link(group = 'globula')
  bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
  bpy.context.object.rigid_body.collision_shape = 'SPHERE'
  bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
  bpy.context.object.constraints['Limit Distance'].target =bpy.data.objects[target]

#add_constraint_between_1_2_spheres
  if len_of_linker == 1:
    bpy.ops.object.empty_add(type = 'PLAIN_AXES', location = (23.5, 0.0, 0.0))
    bpy.ops.rigidbody.constraint_add(type='GENERIC')
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Sphere']



##############____GENERIC____############## set_value_of_all_constraints
#limit_x
    bpy.context.object.rigid_body_constraint.use_limit_lin_x = True
    bpy.context.object.rigid_body_constraint.limit_lin_x_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_x_upper = 0

#limit_y
    bpy.context.object.rigid_body_constraint.use_limit_lin_y = True
    bpy.context.object.rigid_body_constraint.limit_lin_y_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_y_upper = 0

#limit_z
    bpy.context.object.rigid_body_constraint.use_limit_lin_z = True
    bpy.context.object.rigid_body_constraint.limit_lin_z_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_z_upper = 0

#limit_ang_x
    bpy.context.object.rigid_body_constraint.use_limit_ang_x = True
    bpy.context.object.rigid_body_constraint.limit_ang_x_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_x_upper = -1.22173

#limit_ang_y
    bpy.context.object.rigid_body_constraint.use_limit_ang_y = False
    bpy.context.object.rigid_body_constraint.limit_ang_y_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_y_upper = -1.22173

#limit_ang_z
    bpy.context.object.rigid_body_constraint.use_limit_ang_z = False
    bpy.context.object.rigid_body_constraint.limit_ang_z_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_z_upper = -1.22173


###################____CONSTRAINT____########################
  
#add_constraint_between_1_2_spheres
  if len_of_linker == 2 or  len_of_linker == 3 or len_of_linker == 4 or  len_of_linker == 5 or len_of_linker == 6 or  len_of_linker == 7: 
    bpy.ops.object.empty_add(type = 'PLAIN_AXES', location = (23.5, 0.0, 0.0))
    bpy.ops.rigidbody.constraint_add(type='GENERIC')
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.001']
    
##############____GENERIC____##############set_value_of_constraint_between_1 and 2 _spheres
#limit_x
    bpy.context.object.rigid_body_constraint.use_limit_lin_x = True
    bpy.context.object.rigid_body_constraint.limit_lin_x_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_x_upper = 0

#limit_y
    bpy.context.object.rigid_body_constraint.use_limit_lin_y = True
    bpy.context.object.rigid_body_constraint.limit_lin_y_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_y_upper = 0

#limit_z
    bpy.context.object.rigid_body_constraint.use_limit_lin_z = True
    bpy.context.object.rigid_body_constraint.limit_lin_z_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_z_upper = 0

#limit_ang_x
    bpy.context.object.rigid_body_constraint.use_limit_ang_x = True
    bpy.context.object.rigid_body_constraint.limit_ang_x_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_x_upper = -1.22173

#limit_ang_y
    bpy.context.object.rigid_body_constraint.use_limit_ang_y = False
    bpy.context.object.rigid_body_constraint.limit_ang_y_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_y_upper = -1.22173

#limit_ang_z
    bpy.context.object.rigid_body_constraint.use_limit_ang_z = False
    bpy.context.object.rigid_body_constraint.limit_ang_z_lower = -1.22173
    bpy.context.object.rigid_body_constraint.limit_ang_z_upper = -1.22173
   
    

#add_constraint_between_2_3_spheres
  if len_of_linker == 3 or len_of_linker == 4 or len_of_linker == 5 or len_of_linker == 6 or len_of_linker == 7:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere.001']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.002']

#add_constraint_between_3_4_spheres
  if len_of_linker == 4 or len_of_linker == 5 or len_of_linker == 6 or len_of_linker == 7:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere.002']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.003']

#add_constraint_between_4_5_spheres
  if len_of_linker == 5 or len_of_linker == 6 or len_of_linker == 7:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere.003']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.004']

#add_constraint_between_5_6_spheres
  if len_of_linker == 6 or len_of_linker == 7:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere.004']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.005']

#add_constraint_between_6_7_spheres
  if len_of_linker == 7:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Icosphere.005']
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Icosphere.006']

#add_constraint_between__7_spheres_and_globular_domain
  if len_of_linker > 1:
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.translate(value = (3.5, 0, 0))
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects[target]
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Sphere']



#################################________2_layer___________##############

  bpy.ops.object.select_all(action = 'TOGGLE')
  bpy.ops.object.select_all(action = 'TOGGLE')
  bpy.ops.object.duplicate_move()
  bpy.ops.transform.rotate(override, value=0.0349066, axis=(0,0,1))  
#bpy.ops.transform.rotate(override, value=0.0349066, axis=(0,0,1))  
  bpy.ops.transform.translate(value = (0, 0, 4.8), constraint_axis = (False, False, True))


##################-------3_or_more_layers___###################


  for index in range(layers):
#range(1)==3layer, range(2)==4layer,range(3)==5layer,range(4)==6layer,range(5)==7layer,range(6)==8layer...range(90)==92layer,range(98)==100layer
#________3_layer__________
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.rotate(override, value=0.0349066, axis=(0,0,1))  
#bpy.ops.transform.rotate(override, value=0.0349066, axis=(0,0,1))  
    bpy.ops.transform.translate(value = (0, 0, 4.8), constraint_axis = (False, False, True))
  
    


####################_____BAKE_PHYSICS_____#################################

  bpy.ops.ptcache.free_bake_all()
  bpy.ops.ptcache.bake_all(bake=True)
  bpy.ops.screen.frame_jump(end = True)


#########_____JOIN_Globular_domains_######################################

  bpy.ops.object.select_all(action = 'TOGGLE')
  bpy.ops.object.select_same_group(group="globula")
  bpy.context.scene.objects.active = bpy.data.objects["Sphere"]
  bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end = 250, step = 10)
  bpy.ops.object.join()
  bpy.ops.object.editmode_toggle()

#**********************_____CHECK_INTERSECT___*****************
  obj = bpy.context.active_object
  me = obj.data 
  bm = bmesh.from_edit_mesh(me)   
  tree = mathutils.bvhtree.BVHTree.FromBMesh(bm, epsilon=0.00001)

  overlap = tree.overlap(tree)
  faces_error = {i for i_pair in overlap for i in i_pair}
  

#*********______PRINT_TO_FILE_ "+" if in package not intersect**********************

  if len(faces_error)>0:
      print('') 
  else:  
    f1=open(path_to_output_file, 'a+')
    f1.write('+')
    f1.close() 
    
#******************************____OBJECT_MODE____and____DELETE_ALL____******************
  bpy.ops.object.editmode_toggle()
  bpy.ops.object.select_all(action = 'TOGGLE')
  bpy.ops.object.select_all(action = 'TOGGLE')
  bpy.ops.object.delete(use_global=False)  


#******************____Print_to_file_RESULT from all runs____****************

letters = 0 
f= open(path_to_output_file, 'r')
for line in f:
    letters += len(line)
    print("% from 100 runs = ", letters)
    f2 = open(path_to_file_with_result, 'a+')
    f2.write('\n')
    f2.write('\n')
    f2.write('number of monomers = ')
    f2.write(str(layers_up_Z))
    f2.write('\n')    
    f2.write('number of residues in linker = ')
    f2.write(str(len_of_linker))  
    f2.write('\n')  
    f2.write('non intersecting from ')
    f2.write(str(repeat))     
    f2.write(' runs = ')
    f2.write(str(letters))
    f2.close()
f.close()


   
