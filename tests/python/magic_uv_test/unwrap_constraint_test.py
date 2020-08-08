import bpy

from . import common
from . import compatibility as compat


class TestUnwrapConstraint(common.TestBase):
    module_name = "unwrap_constraint"
    idname = [
        # Unwrap Constraint
        ('OPERATOR', 'uv.muv_unwrap_constraint'),
    ]

    def setUpEachMethod(self):
        obj_name = "Cube"

        common.select_object_only(obj_name)
        compat.set_active_object(bpy.data.objects[obj_name])
        bpy.ops.object.mode_set(mode='EDIT')

    def test_ng_no_uv(self):
        print("[TEST] (NG) No UV")
        bpy.ops.mesh.select_all(action='SELECT')
        result = bpy.ops.uv.muv_unwrap_constraint()
        self.assertSetEqual(result, {'CANCELLED'})

    def test_ok_default(self):
        print("[TEST] (OK) Default")
        bpy.ops.mesh.uv_texture_add()
        bpy.ops.mesh.select_all(action='SELECT')
        result = bpy.ops.uv.muv_unwrap_constraint()
        self.assertSetEqual(result, {'FINISHED'})

    def test_ok_user_specified(self):
        print("[TEST] (OK) user specified")
        bpy.ops.mesh.uv_texture_add()
        bpy.ops.mesh.select_all(action='SELECT')
        result = bpy.ops.uv.muv_unwrap_constraint(
            method='CONFORMAL',
            fill_holes=False,
            correct_aspect=False,
            use_subsurf_data=True,
            margin=0.1,
            u_const=True,
            v_const=True
        )
        self.assertSetEqual(result, {'FINISHED'})
