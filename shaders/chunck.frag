#version 330 core

layout (location = 0) out vec4 fragColor;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

uniform sampler2D u_texture_0;

in vec3 voxel_color;
in vec2 uv;

void main() {
    vec3 voxel_color = vec3(1.0, 0.0, 0.0); // Use red color for testing
    fragColor = vec4(voxel_color, 1.0); // Output voxel color
}
