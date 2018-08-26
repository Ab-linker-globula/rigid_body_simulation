import bpy
import os
import sys
import random
import mathutils
import bmesh 

####ATTENTION!  not change position of 3d cursor in the file "start.blend" ! 3D cursor must be in center of 3d view.
#####not change pivot center for rotation/scaling. It must be set as "3D Cursor"


for window in bpy.context.window_manager.windows:
    screen = window.screen
    
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            override = {'window': window, 'screen': screen, 'area': area}
            bpy.ops.screen.screen_full_area(override)
            break

original_type = bpy.context.area.type
bpy.context.area.type = 'VIEW_3D'

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


path = os.path.abspath(os.path.dirname(__file__))
################____________blend.txt___________##################
path_to_output_file = os.path.join(os.path.dirname(__file__),'blend.txt')
################__________radians.txt___________##################

radians = 0.034

################__________repeat.txt___________##################
path_repeat = os.path.join(os.path.split(path)[0],'config.txt')
f = open( path_repeat , 'r')
data = f.read()
first_line = data.split('\n', 1)[0]
x_repeat =first_line.rsplit('=', 1)[1]
repeat = int(x_repeat) 
f.close()

##############___________len_linker.txt____________####################
len_linker_path_to_file= os.path.join(os.path.dirname(__file__),'len_linker.txt')
f = open( len_linker_path_to_file, 'r')
text = f.read()
len_of_linker = int(text)
f.close()
##############___________layer.txt____________####################
layer_path_to_file = os.path.join(os.path.dirname(__file__),'layer.txt')
f = open( layer_path_to_file , 'r')
text1 = f.read()
layer = int(text1)
f.close()

################__________steps_per_second___________##################
path_steps_sec = os.path.join(os.path.split(path)[0],'config.txt')
f = open( path_steps_sec , 'r')
data = f.read()
first_line = data.split('\n', 8)[7]
x_path_steps_sec =first_line.rsplit('=', 1)[1]
steps_per_second = int(x_path_steps_sec) 
f.close()

########__value__constraint_generic_____############
limit_angle = False
limit_lin = True
limit_ang_lower_upper = -1.22173

############################################
for index in range(repeat): 
    
  bpy.data.scenes["Scene"].frame_current = 1

#####################____RANDOM_GRAVITY____#####################
  bpy.context.scene.gravity[2] = random.uniform(-0.5, 0.5)

  bpy.context.scene.gravity[1] = random.uniform(-0.5, 0.5)
  bpy.context.scene.gravity[0] = random.uniform(-0.5, 0.5)
  

#######################____OBJECTS____##############################
#add_cube
  bpy.ops.mesh.primitive_cube_add(radius=1, location = (0.0, 0.0, 0.0))
  bpy.ops.transform.resize(value = (20.0, 11.0, 2.4 ))
  bpy.ops.object.transform_apply(location=False, rotation =False, scale = True)
  bpy.ops.rigidbody.objects_add(type = 'PASSIVE')
  bpy.context.object.rigid_body.collision_shape = 'BOX'

#add_first_sphere_of_linker_passive
  bpy.ops.mesh.primitive_uv_sphere_add(segments = 4,ring_count = 4, size = 1.75, location=(21.75, 0.0, 0.0))
  bpy.ops.rigidbody.objects_add(type = 'PASSIVE')
  bpy.context.object.rigid_body.collision_shape = 'SPHERE'

#add_second_sphere_of_linker_active
  loc_sphere_x = 21.75
  rep = -1
  len_lin = len_of_linker-1
  for index in range(len_lin):
    rep += 1 
    loc_sphere_x += 3.5 
      
    bpy.ops.mesh.primitive_uv_sphere_add(segments = 4,ring_count = 4, size = 1.75, location=(loc_sphere_x, 0.0, 0.0))
    bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
    bpy.context.object.rigid_body.collision_shape = 'SPHERE'
    bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')
    if rep == 0:  
       bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Sphere']
    if rep > 0 :
       str_rep = str(rep)
       bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Sphere.'+str_rep.rjust(3,'0')] 
    
#add_GLOBULAR_DOMAIN
  location_x = loc_sphere_x+ 16.75
  bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=15.0,   location=(location_x, 0.0, 0.0))
########################################
  tar = rep+1
  str_tar = str(tar) 
  bpy.ops.group.create(name = 'globula')
  bpy.ops.object.group_link(group = 'globula')
  bpy.ops.rigidbody.objects_add(type = 'ACTIVE')
  bpy.context.object.rigid_body.collision_shape = 'SPHERE'
  bpy.ops.object.constraint_add(type='LIMIT_DISTANCE')

  if len_of_linker ==1: 
     bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Sphere']  
  elif len_of_linker > 1:      
    bpy.context.object.constraints['Limit Distance'].target = bpy.data.objects['Sphere.'+str_tar.rjust(3,'0')]

  loc_empty_x = 18.25
  rep_e = -1
  for index in range(len_of_linker):

    rep_e += 1
    rep_e_2 = rep_e+1 
    str_ob1 = str(rep_e)
    str_ob2 = str(rep_e_2)
    loc_empty_x += 3.5
    bpy.ops.object.empty_add(type = 'PLAIN_AXES', location = (loc_empty_x, 0.0, 0.0))
    bpy.ops.rigidbody.constraint_add(type='GENERIC')

##############____GENERIC____############## set_value_of_all_constraints
#limit_x
    bpy.context.object.rigid_body_constraint.use_limit_lin_x = limit_lin
    bpy.context.object.rigid_body_constraint.limit_lin_x_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_x_upper = 0

#limit_y
    bpy.context.object.rigid_body_constraint.use_limit_lin_y = limit_lin
    bpy.context.object.rigid_body_constraint.limit_lin_y_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_y_upper = 0

#limit_z
    bpy.context.object.rigid_body_constraint.use_limit_lin_z = limit_lin
    bpy.context.object.rigid_body_constraint.limit_lin_z_lower = 0
    bpy.context.object.rigid_body_constraint.limit_lin_z_upper = 0

#limit_ang_x
    bpy.context.object.rigid_body_constraint.use_limit_ang_x = limit_angle
    bpy.context.object.rigid_body_constraint.limit_ang_x_lower = limit_ang_lower_upper
    bpy.context.object.rigid_body_constraint.limit_ang_x_upper = limit_ang_lower_upper

#limit_ang_y
    bpy.context.object.rigid_body_constraint.use_limit_ang_y = limit_angle
    bpy.context.object.rigid_body_constraint.limit_ang_y_lower = limit_ang_lower_upper
    bpy.context.object.rigid_body_constraint.limit_ang_y_upper = limit_ang_lower_upper

#limit_ang_z
    bpy.context.object.rigid_body_constraint.use_limit_ang_z = limit_angle
    bpy.context.object.rigid_body_constraint.limit_ang_z_lower = limit_ang_lower_upper
    bpy.context.object.rigid_body_constraint.limit_ang_z_upper = limit_ang_lower_upper

    if rep_e ==0:
      bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Sphere']
      bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Sphere.001'] 
    if rep_e > 0:
      bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects['Sphere.'+str_ob1.rjust(3,'0')] 
      bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects['Sphere.'+str_ob2.rjust(3,'0')] 
    
  if layer >1: 
#################################________2_layer___________##############

    bpy.ops.object.select_all(action = 'SELECT')
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.rotate(override, value=radians, axis=(0,0,1))   
    bpy.ops.transform.translate(value = (0, 0, 4.8), constraint_axis = (False, False, True))

  layer_up = layer - 2

  if layer>2:
     for index in range(layer_up):
##################-------3_or_more_layers___###################
        bpy.ops.object.duplicate_move()
        bpy.ops.transform.rotate(override, value= radians, axis=(0,0,1))    
        bpy.ops.transform.translate(value = (0, 0, 4.8), constraint_axis = (False, False, True))
  
####################_____BAKE_PHYSICS_____#################################

###test
  bpy.context.scene.rigidbody_world.steps_per_second = steps_per_second
###test

  bpy.data.scenes['Scene'].rigidbody_world.time_scale = 2.000
  bpy.ops.ptcache.free_bake_all()
  bpy.ops.ptcache.bake_all(bake=True)
  bpy.ops.screen.frame_jump(end = True)

#########_____JOIN_Globular_domains_######################################
  str_linker = str(len_of_linker)
  bpy.ops.object.select_all(action = 'DESELECT')
  bpy.ops.object.select_same_group(group="globula")
  bpy.context.scene.objects.active = bpy.data.objects['Sphere.'+str_linker.rjust(3,'0')] 
  bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end = 251, step = 50)

  if layer == 1:
        f1=open(path_to_output_file, 'a+')
        f1.write('+')
        f1.close()     

  if layer > 1 :
  
    bpy.ops.object.join()
    bpy.ops.object.editmode_toggle()

#**********************_____CHECK_INTERSECT___BETWEEN_globular_domain*****************
    obj = bpy.context.active_object
    me = obj.data 
    bm = bmesh.from_edit_mesh(me)   
    tree = mathutils.bvhtree.BVHTree.FromBMesh(bm, epsilon=0.00001)

    overlap = tree.overlap(tree)
    faces_error = {i for i_pair in overlap for i in i_pair}

#*********___print_result_to blend.txt__**********************

    if len(faces_error)>0:
        print('') 
    else:  
        f1=open(path_to_output_file, 'a+')
        f1.write('+')
        f1.close() 

#******************************____OBJECT_MODE____and____DELETE_ALL____******************
    
    bpy.ops.object.editmode_toggle()     
  bpy.ops.object.select_all(action = 'SELECT')
  bpy.ops.object.delete(use_global=False)
    
bpy.ops.wm.quit_blender()   
  

