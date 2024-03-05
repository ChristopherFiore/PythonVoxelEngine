from settings import *

def is_void(voxel_pos, chunck_voxels):
    x, y, z = voxel_pos
    if 0 <= x < CHUNCK_SIZE and 0 <= y < CHUNCK_SIZE and 0 <= z < CHUNCK_SIZE:
        if chunck_voxels[x + CHUNCK_SIZE * z + CHUNCK_AREA * y]:
            return False
    return True

def add_data(vertex_data, index, *vertices):
    for vertex in vertices:
        for attr in vertex:
            vertex_data[index] = attr
            index += 1
    return index

def build_chunck_mesh(chunck_voxels, format_size):
    vertex_data = np.empty(CHUNCK_VOL * 18 * format_size, dtype='uint8')
    index = 0

    for x in range(CHUNCK_SIZE):
        for y in range(CHUNCK_SIZE):
            for z in range(CHUNCK_SIZE):
                voxel_id = chunck_voxels[x + CHUNCK_SIZE * z + CHUNCK_AREA * y]
                if not voxel_id:
                    continue

                # Top face
                if is_void((x, y + 1, z), chunck_voxels):
                    # Format: x, y, z, voxel_id, face_id
                    v0 = (x    , y + 1, z    , voxel_id, 0)
                    v1 = (x + 1, y + 1, z    , voxel_id, 0)
                    v2 = (x + 1, y + 1, z + 1, voxel_id, 0)
                    v3 = (x    , y + 1, z + 1, voxel_id, 0)

                    index = add_data(vertex_data, index, v0, v3, v2, v0, v2, v1)

                # Bottom Face
                if is_void((x, y - 1, z), chunck_voxels):
                    v0 = (x, y, z, voxel_id, 1)
                    v1 = (x + 1, y, z, voxel_id, 1)
                    v2 = (x + 1, y, z + 1, voxel_id, 1)
                    v3 = (x, y, z + 1, voxel_id, 1)

                    index = add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)

                # Right Face
                if is_void((x + 1, y, z), chunck_voxels):
                    v0 = (x + 1, y, z, voxel_id, 2)
                    v1 = (x + 1, y + 1, z, voxel_id, 2)
                    v2 = (x + 1, y + 1, z + 1, voxel_id, 2)
                    v3 = (x + 1, y, z + 1, voxel_id, 2)

                    index = add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)

                # Left Face
                if is_void((x - 1, y, z), chunck_voxels):
                    v0 = (x, y, z, voxel_id, 3)
                    v1 = (x, y + 1, z, voxel_id, 3)
                    v2 = (x, y + 1, z + 1, voxel_id, 3)
                    v3 = (x, y, z + 1, voxel_id, 3)

                    index = add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)
                
                # Back Face
                if is_void((x, y, z - 1), chunck_voxels):
                    v0 = (x, y, z, voxel_id, 4)
                    v1 = (x, y + 1, z, voxel_id, 4)
                    v2 = (x + 1, y + 1, z, voxel_id, 4)
                    v3 = (x + 1, y, z, voxel_id, 4)

                    index = add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)
                
                # Front Face
                if is_void((x, y, z + 1), chunck_voxels):
                    v0 = (x, y, z + 1, voxel_id, 5)
                    v1 = (x, y + 1, z + 1, voxel_id, 5)
                    v2 = (x + 1, y + 1, z + 1, voxel_id, 5)
                    v3 = (x + 1, y, z + 1, voxel_id, 5)

                    index = add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)

    return vertex_data[:index + 1]




















                
