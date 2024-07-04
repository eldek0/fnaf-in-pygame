#version 330 core
uniform sampler2D image;

out vec4 color;
in vec2 fragmentTexCoord;

void main()
{
    vec2 fragCoord = fragmentTexCoord.xy;
    highp float y_pos = fragCoord.y * 100;

    if (mod(y_pos, 1.3) < 1)
    {
        discard;
    }
    
    color = texture(image, fragmentTexCoord);
}