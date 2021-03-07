function Submit() {
    let bx = parseFloat(document.getElementById("bx").value);
    let bz = parseFloat(document.getElementById("bz").value);
    let tx = parseFloat(document.getElementById("tx").value);
    let tz = parseFloat(document.getElementById("tz").value);

    let dist = Math.sqrt(Math.pow(bx - tx, 2) + Math.pow(bz - tz, 2));

    let dir_x = - (bx - tx) / dist;
    let dir_y = (bz - tz) / dist;

    let angle = Math.atan2(dir_y , dir_x) + Math.PI;

    let angle_degree = (angle / Math.PI) * 180;

    document.getElementById("angle").value = Math.round(angle_degree) + " °";

    document.getElementById("distance").value = Math.round(dist) + " meters";

    return false;
}