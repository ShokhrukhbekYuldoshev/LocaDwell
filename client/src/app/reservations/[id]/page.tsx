export default function ReservationDetailsPage({
    params,
}: {
    params: { id: string };
}) {
    const { id } = params;
    return <div>ReservationDetailsPage id: {id}</div>;
}
