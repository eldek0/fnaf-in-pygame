#version 330 core
uniform sampler2D image;

out vec4 color;
in vec2 fragmentTexCoord;

void main() {

    float stripWidth = 1.0;

    float strip = mod(fragmentTexCoord.y, stripWidth);

    if (strip <= stripWidth){
        color = texture(image, fragmentTexCoord);
    }
    else{
        color = vec4(1.0, 0.0, 0.0, 1.0);
    }

}