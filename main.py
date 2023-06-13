from rigid_body_trans_class import RigidBodyTrans
from dataset_examples import Torus
from viewer import Viewer3D

if __name__ == "__main__":

    t1 = Torus(num_of_points=100)
    t2 = t1.create_shifted_torus()
    rbt_instance = RigidBodyTrans(p=t1.torus, q=t2.torus)
    rbt_instance.calc_transformation()
    Viewer3D.plot(t1, t2, rbt=rbt_instance)