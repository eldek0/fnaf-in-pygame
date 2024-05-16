#version 330 core

in vec3 fragmentColor;
in vec2 fragmentTexCoord;

out vec4 color;

uniform sampler2D imageTexture;

void main() {
    vec4 sepia = vec4(1.2, 1.0, 0.8, 1.0);
    color = texture(imageTexture, fragmentTexCoord)*sepia;
}